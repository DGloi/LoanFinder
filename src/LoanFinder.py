"""Welcome to LoanFinder !
LoanFinder si a small command line app that retrieves loans from an existing list 
on which a user can apply, depending on his project and his financial situation.

"""

#importing libraries
from importlib.resources import path
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


def get_user_info():
    debt = q.text("What's your current amount of monthly debt?").ask()
    income = q.text("What's your total monthly income?").ask()
    loan_amount = q.text("What's your desired loan amount?").ask()
    home_value = q.text("What's your home value?").ask()

    debt=float(debt)
    income=float(income)
    loan_amount=float(loan_amount)
    home_value=float(home_value)

    return debt,income,loan_amount,home_value


def import_banks_data():
    csvpath=q.text("Please provide banks info file location (.csv) ").ask()
    csvpath=Path(csvpath)  
    

    if not csvpath.exists():
        sys.exit(f"File not found on this  directory: {csvpath}")
    return import_csv(csvpath)


def elligible_loans(banks_data,debt,income,loan_amount,home_value):
    
    #calculate user's debt ratio and
    debt_ratio=monthly_debt_ratio(debt,income)
    print(f"The monthly debt to income ratio is {debt_ratio:.02f}")
    loan_to_value=loan_to_value_ratio(loan_amount,home_value)
    print(f"The loan to value ration is {loan_to_value:.02f}")

    #filter bank data applicable
    filtered_bank_data=filter_max_loan_size(loan_amount,banks_data) 
    filtered_bank_data=filter_loan_to_value(loan_to_value,filtered_bank_data)
    filtered_bank_data=filter_debt_to_income(debt_ratio,filtered_bank_data)

    print(f"Found {len(filtered_bank_data)} qualifying loans")

    return filtered_bank_data 

def saving_elligible_loans(elligible_loans_list):

    if len (elligible_loans_list)== 0:
        sys.exit ("It seems that in your current situation, you are not elligible for any loans in the provided list..")
    if len (elligible_loans_list)>=1:
        action=q.select(
        "Do you want to save your list of qualifying loans as a .csv file?", choices=["yes", "no"],).ask()

        if action =="yes":

            save_csv=q.text("Enter a file path to a rate-sheet (.csv):").ask()
            save_csv=Path(save_csv)
            header=[
                "Bank","Max loan amount","Max Loan to value ratio","Max debt to income ratio","Interest rate"
                ]

            with open (save_csv, "w",newline="") as csvfile:

             csvwriter = csv.writer(csvfile)
             csvwriter.writerow(header)

             for elligible_loan in elligible_loans_list:
                csvwriter.writerow(elligible_loan)
            
            print(f"Your list of potential loans is to be found here: {save_csv} ")
            print("We hope you liked using our app, see you soon.")
            sys.exit

            if not save_csv.exists():
                sys.exit(f"Sorry, this path does not exist: {save_csv}")

        elif action=="no":
            sys.exit("Thanks for using the App, we hope to see you soon")


def run_app():

    banks_data=import_banks_data()

    debt,income,loan_amount,home_value=get_user_info()

    elligible_loans_list=elligible_loans(
        banks_data,debt,income,loan_amount,home_value
        )

    saving_elligible_loans(elligible_loans_list)



if __name__=="__main__":
    fire.Fire(run_app)
