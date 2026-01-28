from django.contrib import admin
from .models import TaxPayerProfile, TaxReturn, Alert, Document, Payment, AuditLog

# 1. Profile Admin
class TaxPayerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'pan_number', 'phone')

# 2. Tax Return Admin
class TaxReturnAdmin(admin.ModelAdmin):
    list_display = ('taxpayer', 'financial_year', 'gross_income', 'total_tax', 'status')
    list_filter = ('status', 'financial_year')

# 3. Payment Admin
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'amount', 'status', 'payment_date')

# 4. Audit Log Admin
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    readonly_fields = ('timestamp',) # Logs shouldn't be editable

# Register all models
admin.site.register(TaxPayerProfile, TaxPayerProfileAdmin)
admin.site.register(TaxReturn, TaxReturnAdmin)
admin.site.register(Alert)
admin.site.register(Document)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(AuditLog, AuditLogAdmin)