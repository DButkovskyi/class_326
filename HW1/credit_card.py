"""Perform credit card calculations."""
from argparse import ArgumentParser
import sys


MIN_PERCENT = 0.02
YEAR_DAYS = 365
CYCLE_DAYS = 30

def get_min_payment(balance, fees = 0):
    """
    Calculates the minimum monthly payment for a credit card balance.
    Args:
        balance (float): The current balance on the credit card.
        fees (float, optional): Additional fees to be included in the minimum payment. Default is 0.
    Returns:
        float: The minimum monthly payment, which is either 2% of the balance plus fees or $25, whichever is greater.
    """

    min_payment = ((balance * MIN_PERCENT) + fees)
    if (min_payment > 25):
        return min_payment
    else:
        return 25


def interest_charged(balance, apr):
    """
    Calculates the monthly interest charged on a credit card balance.
    Args:
        balance (float): The current balance on the credit card.
        apr (float): The annual percentage rate (APR) as a int.
    Returns:
        float: The monthly interest charged on the balance.
    """


    #converts int APR into percent
    apr = apr/100
    interest = (apr/YEAR_DAYS) * balance * CYCLE_DAYS

    return interest


def remaining_payments(balance, apr, targetamount = None, credit_line = 5000, fees = 0):
    """
    Calculate the number of payments needed to pay off a credit card balance and track thresholds.
    Args:
        balance (float): The current balance on the credit card.
        apr (float): The annual percentage rate (APR) as int
        targetamount (float, optional): The desired monthly payment amount. If None, minimum payment is used. Default is None.
        credit_line (float, optional): The credit card's credit line. Default is 5000.
        fees (float, optional): Additional fees to be included in the payments. Default is 0.
    Returns:
        tuple: A tuple containing the following values:
            - int: The number of payments needed to pay off the balance.
            - int: The number of months the balance exceeded 25% of the credit line.
            - int: The number of months the balance exceeded 50% of the credit line.
            - int: The number of months the balance exceeded 75% of the credit line.
    """
    
    payment_count = 0
    balance_over_25 = 0
    balance_over_50 = 0
    balance_over_75 = 0
    payment = targetamount

    while(balance > 0):
        if (targetamount is None):
            payment = get_min_payment(balance, fees)
        
        interest_payment = interest_charged(balance, apr)
        payment_toward_balance = payment - interest_payment

        if (payment_toward_balance < 0):
            print("Card balance cannot be paid off")
            break
    
        balance = balance - payment_toward_balance

        if (balance > credit_line * 0.75):
            balance_over_75 += 1
            balance_over_50 += 1
            balance_over_25 += 1
        elif (balance > credit_line * 0.5):
            balance_over_50 += 1
            balance_over_25 += 1
        elif (balance > credit_line * 0.25):
            balance_over_25 += 1
        
        payment_count += 1

    return payment_count, balance_over_25, balance_over_50, balance_over_75


def main(balance, apr, credit_line = 5000, targetamount = None, fees = 0):
    """
    Calculate credit card payment information.
    Args:
        balance (float): The current balance on the credit card.
        apr (float): The annual percentage rate (APR) as int
        credit_line (float, optional): The credit card's credit line. Default is 5000.
        targetamount (float, optional): The desired monthly payment amount. If None, minimum payment will be used. Default is None.
        fees (float, optional): Additional fees to be included in the payments. Default is 0.
    Returns:
        str: A formatted string with payment information and balance thresholds.
    """

    recommended_minimum_payment = get_min_payment(balance,fees)
    print(f"Your recommended starting minimum payment is ${recommended_minimum_payment}.")

    pays_minimum = False

    if (targetamount is None):
        pays_minimum = True
    elif (targetamount < recommended_minimum_payment):
        print("Your target payment is less than the minimum payment for this credit card")
        sys.exit(0)
    
    if (pays_minimum):
        remaining_payment = remaining_payments(balance, apr, targetamount, credit_line, fees)
        print(f"If you pay the minimum payments each month, you will pay off the balance in {remaining_payment[0]} payments\n")
    else:
        remaining_payment = remaining_payments(balance, apr, targetamount, credit_line, fees)
        print(f"If you make payments of ${targetamount}, you will pay off the balance in {remaining_payment[0]} payments.")

    return f"You will spend a total of {remaining_payment[1]} months over 25% of the credit line\nYou will spend a total of {remaining_payment[2]} months over 50% of the credit line\nYou will spend a total of {remaining_payment[3]} months over 75% of the credit line"


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
    arguments
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    parser = ArgumentParser()
    parser.add_argument('balance_amount', type = float, help = 'The total amount of balance left on the credit account')
    parser.add_argument('apr', type = int, help = 'The annual APR, should be an int between 1 and 100')
    parser.add_argument('credit_line', type = int, help = 'The maximum amount of balance allowed on the credit line.')
    parser.add_argument('--payment', type = int, default = None, help = 'The amount the user wants to pay per payment, should be a positive number')
    parser.add_argument('--fees', type = float, default = 0, help = 'The fees that are applied monthly.')
    # parse and validate arguments
    args = parser.parse_args(args_list)
    if args.balance_amount < 0:
        raise ValueError("balance amount must be positive")
    if not 0 <= args.apr <= 100:
        raise ValueError("APR must be between 0 and 100")
    if args.credit_line < 1:
        raise ValueError("credit line must be positive")
    if args.payment is not None and args.payment < 0:
        raise ValueError("number of payments per year must be positive")
    if args.fees < 0:
        raise ValueError("fees must be positive")
    return args

if __name__ == "__main__":
    try:
        arguments = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    print(main(arguments.balance_amount, arguments.apr, credit_line = arguments.credit_line, targetamount = arguments.payment, fees = arguments.fees))