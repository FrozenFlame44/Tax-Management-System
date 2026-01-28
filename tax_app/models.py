from django.db import models
from django.contrib.auth.models import User

# 1. Tax Payer Profile (Matches Report Pg 11)
class TaxPayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pan_number = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

# 2. Tax Return (Matches Report Pg 12)
class TaxReturn(models.Model):
    STATUS_CHOICES = [('PENDING', 'Pending'), ('APPROVED', 'Approved')]
    
    taxpayer = models.ForeignKey(TaxPayerProfile, on_delete=models.CASCADE)
    financial_year = models.CharField(max_length=9, default="2025-2026")
    salary_income = models.DecimalField(max_digits=12, decimal_places=2)
    other_income = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # Auto-calculated fields
    gross_income = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    total_tax = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    
    filing_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.financial_year} - {self.status}"

# 3. Alert (Matches Report Pg 13) - FIXED INDENTATION
class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.user.username}: {self.message}"

# 4. Document (Matches Report Pg 11)
class Document(models.Model):
    DOC_TYPES = [
        ('W2', 'W-2 Form'),
        ('1040', '1040 Form'),
        ('RECEIPT', 'Receipt/Invoice'),
        ('ID', 'Identity Proof'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=50, choices=DOC_TYPES)
    file = models.FileField(upload_to='user_docs/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename

# 5. Payment (Matches Report Pg 12)
class Payment(models.Model):
    tax_return = models.OneToOneField(TaxReturn, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default='Success')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payment_id} - {self.status}"

# 6. Audit Log (Matches Report Pg 13)
class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)