"""
calculation.py calculates multiple financial ratio  needed 
to determine if one can apply to a loan or not
"""

def monthly_debt_ratio(monthly_debt_payment, monthly_income):
    monthly_debt_ratio= int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio


def loan_to_value_ratio (loan_amount,home_value):
    loan_to_value_ratio= int(loan_amount)/int(home_value)
    return loan_to_value_ratio
