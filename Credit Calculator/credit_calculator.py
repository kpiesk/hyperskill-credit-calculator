import argparse
import math
import sys


def credit_calculator():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, help='type of payment')
    parser.add_argument('--principal', type=float,
                        help='your credit principal')
    parser.add_argument('--payment', type=float, help='your monthly payment')
    parser.add_argument('--periods', type=int,
                        help='number of months needed to repay the credit')
    parser.add_argument('--interest', type=float, help='interest rate')
    args = parser.parse_args()

    if len(sys.argv) != 5 or check_negative_values(
            [args.principal, args.payment, args.periods, args.interest]):
        print('Incorrect parameters')
    else:
        if args.type == 'annuity':
            if args.principal is None:
                calc_credit_principal(
                    args.payment, args.periods, args.interest)
            elif args.payment is None:
                calc_monthly_payment(
                    args.principal, args.periods, args.interest)
            elif args.periods is None:
                calc_periods(args.principal, args.payment, args.interest)
            else:
                print('Incorrect parameters')
        elif args.type == 'diff' and args.payment is None:
            calc_diff_payment(args.principal, args.periods, args.interest)
        else:
            print('Incorrect parameters')


# returns True if there are negative values in the passed arguments
def check_negative_values(arguments):
    for arg in arguments:
        if arg is not None and arg < 0:
            return True
    return False


# calculates the nominal interest rate
def calc_nominal_interest(credit_interest):
    return credit_interest / (12 * 100)


# calculates the count of periods for annuity payment
def calc_periods(credit_principal, monthly_payment, credit_interest):
    i = calc_nominal_interest(credit_interest)
    periods = math.ceil(
        math.log((monthly_payment
                  / (monthly_payment - i * credit_principal)), 1 + i))

    years = periods // 12
    months = periods % 12

    overpayment = math.ceil(monthly_payment * periods - credit_principal)

    if months == 0:
        years_string = '1 year' if years == 1 else f'{years} years'
        print(f'You need {years_string} to repay this credit!')
    elif years == 0:
        months_string = '1 month' if months == 1 else f'{months} months'
        print(f'You need {months_string} to repay this credit!')
    else:
        years_string = '1 year' if years == 1 else f'{years} years'
        months_string = '1 month' if months == 1 else f'{months} months'
        print(f'You need {years_string} and {months_string} '
              f'to repay this credit!')

    print(f'Overpayment = {overpayment}')


# calculates monthly payment for annuity payment
def calc_monthly_payment(credit_principal, periods, credit_interest):
    i = calc_nominal_interest(credit_interest)
    pow_result = math.pow(1 + i, periods)

    monthly_payment = math.ceil(
        credit_principal * ((i * pow_result) / (pow_result - 1)))

    overpayment = math.ceil(monthly_payment * periods - credit_principal)

    print(f'Your annuity payment = {monthly_payment}!\n'
          f'Overpayment = {overpayment}')


# calculates the credit principal for annuity payment
def calc_credit_principal(monthly_payment, periods, credit_interest):
    i = calc_nominal_interest(credit_interest)
    pow_result = math.pow(1 + i, periods)

    credit_principal = math.floor(
        monthly_payment / ((i * pow_result) / (pow_result - 1)))

    overpayment = math.ceil(monthly_payment * periods - credit_principal)

    print(f'Your credit principal = {credit_principal}!\n'
          f'Overpayment = {overpayment}')


# calculates the differentiated payment
def calc_diff_payment(credit_principal, periods, credit_interest):
    i = calc_nominal_interest(credit_interest)
    payments_sum = 0

    for month in range(1, periods + 1):
        monthly_payment = math.ceil(
            credit_principal / periods + i *
            (credit_principal - ((credit_principal * (month - 1)) / periods)))

        payments_sum += monthly_payment
        print(f'Month {month}: paid out {monthly_payment}')

    overpayment = math.ceil(payments_sum - credit_principal)
    print(f'\nOverpayment = {overpayment}')


credit_calculator()
