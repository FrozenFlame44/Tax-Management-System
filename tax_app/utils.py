from decimal import Decimal

def calculate_tax(salary, other):
    gross = Decimal(salary) + Decimal(other)
    taxable = gross - Decimal(50000) # Standard Deduction
    
    if taxable < 0: taxable = Decimal(0)
    
    tax = Decimal(0)
    remaining = taxable

    # Slab 1: 0-3L (0%)
    if remaining > 300000:
        remaining -= 300000
    else:
        return {'gross': gross, 'tax': 0}

    # Slab 2: 3L-6L (5%)
    slab_amount = min(remaining, 300000)
    tax += slab_amount * Decimal(0.05)
    remaining -= slab_amount

    # Slab 3: >6L (Simple logic for project: Flat 10% on rest)
    if remaining > 0:
        tax += remaining * Decimal(0.10)

    return {'gross': gross, 'tax': round(tax, 2)}