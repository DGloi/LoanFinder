"""Welcome to LoanFinder !
LoanFinder si a small command line app that retrieves loans from an existing list 
on which a user can apply, depending on his project and his financial situation.

"""

#importing libraries
import sys
import csv
import fire
import questionary
from pathlib import Path

#importing created functions

from utils.file_import import import_csv
from calc.calculations import (
    
)
from filter.debt_to_income import filter_debt_to_income
from filter.loan_to_value import filter_loan_to_value
from filter.max_loan_size import filter_max_loan_size