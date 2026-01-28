from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.template.loader import get_template
from django.http import HttpResponse
from io import BytesIO
from xhtml2pdf import pisa
import uuid

# --- IMPORT ALL YOUR MODELS HERE ---
# [cite_start]Added Alert, AuditLog, and Payment to match your Report [cite: 238, 241, 243]
from .models import TaxReturn, TaxPayerProfile, Alert, AuditLog, Payment
from .forms import TaxReturnForm
from .utils import calculate_tax

# --- AUTHENTICATION ---
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create default profile
            TaxPayerProfile.objects.create(user=user, pan_number=f"PAN{user.id}", phone="0000000000", address="Update Needed")
            
            # [cite_start]Log the action [cite: 243]
            AuditLog.objects.create(user=user, action="New User Registered")
            
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'tax_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # [cite_start]Log the action [cite: 243]
            AuditLog.objects.create(user=user, action="User logged in")
            
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'tax_app/login.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        # [cite_start]Log the action before logout [cite: 243]
        AuditLog.objects.create(user=request.user, action="User logged out")
    logout(request)
    return redirect('login')

# --- CORE LOGIC ---
@login_required
def dashboard(request):
    returns = TaxReturn.objects.filter(taxpayer=request.user.taxpayerprofile)
    
    # [cite_start]Fetch alerts for the "Receive Alerts" use case [cite: 63]
    alerts = Alert.objects.filter(user=request.user, is_read=False)
    
    return render(request, 'tax_app/dashboard.html', {
        'returns': returns,
        'alerts': alerts
    })

@login_required
def file_return(request):
    if request.method == 'POST':
        form = TaxReturnForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.taxpayer = request.user.taxpayerprofile
            
            # [cite_start]Run Calculation [cite: 19]
            result = calculate_tax(obj.salary_income, obj.other_income)
            obj.gross_income = result['gross']
            obj.total_tax = result['tax']
            
            obj.save()
            
            # [cite_start]Log the action [cite: 243]
            AuditLog.objects.create(user=request.user, action=f"Filed Return for {obj.financial_year}")
            
            return redirect('dashboard')
    else:
        form = TaxReturnForm()
    return render(request, 'tax_app/file_return.html', {'form': form})

# --- PDF GENERATION ---
@login_required
def download_receipt(request, id):
    tax_return = get_object_or_404(TaxReturn, id=id, taxpayer=request.user.taxpayerprofile)
    template = get_template('tax_app/receipt_pdf.html')
    html = template.render({'return': tax_return})
    result = BytesIO()
    pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    return HttpResponse(result.getvalue(), content_type='application/pdf')

# --- PAYMENT SIMULATION ---
@login_required
def make_payment(request, return_id):
    # Ensure the return belongs to the logged-in user
    tax_return = get_object_or_404(TaxReturn, id=return_id, taxpayer=request.user.taxpayerprofile)
    
    # [cite_start]Create payment record as per report schema [cite: 238]
    Payment.objects.create(
        tax_return=tax_return,
        payment_id=f"PAY-{uuid.uuid4().hex[:8].upper()}",
        amount=tax_return.total_tax,
        status='Success'
    )
    
    # Update return status
    tax_return.status = 'APPROVED'
    tax_return.save()
    
    # [cite_start]Log the action [cite: 243]
    AuditLog.objects.create(user=request.user, action=f"Payment made for Return #{return_id}")
    
    return redirect('dashboard')