"""Welcome to LoanFinder !
LoanFinder si a small command line app that retrieves loans from an existing list 
on which a user can apply, depending on his project and his financial situation.

"""

#importing libraries
from mmap import PAGESIZE
import sys
import csv
import fire
import questionary as q
from pathlib import Path

#importing created functions

from utils.file_import import import_csv
from calc.calculations import (
    monthly_debt_ratio,
    loan_to_value_ratio
)
from filter.debt_to_income import filter_debt_to_income
from filter.loan_to_value import filter_loan_to_value
from filter.max_loan_size import filter_max_loan_size

if __name__=="__main__":
    fire.Fire(run_app)

def get_user_info():
    debt = q.text("What's your current amount of monthly debt?").ask()
    income = q.text("What's your total monthly income?").ask()
    loan_amount = q.text("What's your desired loan amount?").ask()
    home_value = q.text("What's your home value?").ask()


def banks_data():
    csvpath=q.text("Please provide banks info file location (.csv) ")
    csvpath=Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"File not found on this  directory: {csvpath}")
    return import_csv(csvpath)

def run():
    debt,income,loan_amount,home_value=get_user_info()
    
    sentence="Thanks for using LoanFinder, we hope you found what you need."
    return sentence 
