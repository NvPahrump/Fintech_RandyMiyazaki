# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""

print(" ")
print("part 1: Automate the Calculations.")

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
#
# Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
_len = len(loan_costs)
print("number of loans:", _len)

# What is the total of all loans?
#
# Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
_sum = sum(loan_costs)
print(f"sum of all loans: {_sum:.2f}")

# What is the average loan amount from the list?
#
# Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
_avg = _sum / _len
print(f"average loan amount: {_avg:.2f}")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

print(" ")
print("part 2: Analyze Loan Data")

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.

print(f'Loan Price: {loan.get("loan_price"):.2f}')
print('Remaining Months: ' + str(loan.get("remaining_months")))
print('Repayment Interval: ' + str(loan.get("repayment_interval")))
print(f'Future Value: {loan.get("future_value"):.2f}')

# Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

_discount_rate = .20

_present_value = loan.get("future_value") / (1 + _discount_rate / 12) ** loan.get("remaining_months")

print("Present Value: " + str(round(_present_value, 2)))

if _present_value > loan.get("loan_price"):
    print("Buy! It's worth more than it's selling for.")

elif _present_value < loan.get("loan_price"):
    print("Don't buy! as it's offered at a price higher than what it's worth.")

elif _present_value == loan.get("loan_price"):
    print("Breakeven case! You can expect to earn exactly your hurdle rate on this deal.")

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""
print(" ")
print("part 3: Perform Financial Calculations")

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"future_value: {future_value:.2f}")
print("remaining_months:", remaining_months)

# Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

def calc_present_value(_future_value, _remaining_months, _annual_discount_rate):    

   return _future_value / (1 + _annual_discount_rate / 12) ** _remaining_months

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

annual_discount_rate = 0.2

present_value = round(calc_present_value(future_value, remaining_months, annual_discount_rate), 2)

print(f'The present value of the loan is: {present_value:.2f} the selling price is: {new_loan.get("loan_price"):.2f}')

if present_value > new_loan.get("loan_price"):
    print("Buy! It's worth more than it's selling for.")

elif _present_value < new_loan.get("loan_price"):
    print("Don't buy! as it's offered at a price higher than what it's worth.")

elif _present_value == new_loan.get("loan_price"):
    print("Breakeven case! You can expect to earn exactly your hurdle rate on this deal.")

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""
print(" ")
print("part 4: Conditionally Filter Lists of Loans")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for item in loans:
    if (item["loan_price"] <= 500):
        inexpensive_loans.append(item)

# Print the `inexpensive_loans` list
print("inexpensive_loans:")
for item in inexpensive_loans:
    print(item)

"""Part 5: Save the results.

Output this list of inexpensiveexpensive_loans` list
print(" ")
i = len(inexpensive_loans)
while i:
    print(inexpensive_loa loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

print(" ")
print("part 5: Save the Results")

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path('c:/Users/Broth/Fintech_RandyMiyazaki/Module_1_Challenge/inexpensive_loans.csv')

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, "w") as csvfile:
   
    # Create a csvwriter   
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Write the header to the CSV file
    csvwriter.writerow(header)

    # Write the values of each dictionary inside of `big_raisers`
    # as a row in the CSV file.
    for item in inexpensive_loans:
        csvwriter.writerow(item.values())

print("Inexpensive Loans saved to CSV file inexpensive_loans.csv")

print("")
print("DONE")








