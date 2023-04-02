# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""

import sys
import csv
import fire
import questionary

from pathlib import Path

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    # test
     
    #csvpath = Path("c:/Users/Broth/FinTech/2Module2Challenge/RandyMiyazaki/loan_qualifier_app/data/daily_rate_sheet.csv")
   
    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)

    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    # test
    #credit_score = 600
    #debt = 1000
    #income = 5000
    #loan_amount = 50000
    #home_value = 200000

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio:\t{monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio:\t\t{loan_to_value_ratio:.02f}")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    return bank_data_filtered

def display_csv(qualifying_loans):

    # no test
    return

    # test

    print(f"The number of qualifying loans:\t\t{len(qualifying_loans)}\n")
    #print("Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate")
    for item in qualifying_loans:
        print(f"Lender:\t\t\t{item[0]}")
        print(f"Max Loan Amount:\t{item[1]}")
        print(f"Max LTV:\t\t{item[2]}")
        print(f"Min DTI:\t\t{item[3]}")
        print(f"Min Credit Score:\t{item[4]}")
        print(f"Interest Rate:\t\t{item[5]}%\n")

def save_qualifying_loans(qualifying_loans):

    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """

    #3 Given that I have a list of qualifying loans, when I’m prompted to save the results, then I should be able to opt out of saving the file.
    
    answer = questionary.confirm("Do you want to save the Qualifying Loans to a file?").ask()
    if answer == False:
        return
    
    # test
    #output_path = ("c:/Users/Broth/FinTech/2Module2Challenge/RandyMiyazaki/loan_qualifier_app/qualifying_loans.csv")  

    #1 Given that I’m using the loan qualifier CLI, when I run the qualifier, then the tool should prompt the user to save the results as a CSV file.    
    #4 Given that I have a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file.  
     
    output_path = questionary.text("Enter a file path for Qualified Loan (.csv) or hit ENTER for none:").ask()
        
    if len(output_path) == 0:    

        return("")
        
    # Use the csv library and `csv.writer` to write the header row and each row of `items` from the `qualifying loans` list.

    #5 Given that I’m using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file.

    i = output_path.rfind(".csv")
    if i <= 0:
        output_path = output_path + ".csv"
    
    with open(output_path, "w") as csvfile:
   
        # Create a csvwriter   
        csvwriter = csv.writer(csvfile, delimiter=",")

        header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]

        # Write the header to the CSV file
        csvwriter.writerow(header)

        # Write the values of each dictionary inside of `big_raisers` as a row in the CSV file.
        for item in qualifying_loans:
            csvwriter.writerow(item)
            
        print(f"Wrote File {output_path}")
    
        return(output_path)
    
def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    #2 Given that no qualifying loans exist, when prompting a user to save a file, then the program should notify the user and exit.
   
    if len(qualifying_loans) == 0:  

        print("\nNO qualifying loans exist")
        exit()

    else:

        # Display qualifying loans
        display_csv(qualifying_loans)

        #0 As a user, I need the ability to save the qualifying loans to a CSV file so that I can share the results as a spreadsheet.       

        # Save qualifying loans
        save_qualifying_loans(qualifying_loans)

if __name__ == "__main__":
    fire.Fire(run)
