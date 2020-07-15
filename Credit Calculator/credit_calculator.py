import math


def credit_calculator():
    action = input('What do you want to calculate?'
                   '\ntype "n" - for count of months:'
                   '\ntype "a" - for annuity monthly payment:'
                   '\ntype "p" - for credit principal:\n')
    if action == 'n':
        count_months(float(input('Enter credit principal:\n')),
                     float(input('Enter monthly payment:\n')),
                     float(input('Enter credit interest:\n')))
    elif action == 'a':
        count_monthly_payment(float(input('Enter credit principal:\n')),
                              float(input('Enter count of periods:\n')),
                              float(input('Enter credit interest:\n')))
    elif action == 'p':
        count_credit_principal(float(input('Enter monthly payment:\n')),
                               float(input('Enter count of periods:\n')),
                               float(input('Enter credit interest:\n')))


def count_months(credit_principal, monthly_payment, credit_interest):
    i = get_nominal_interest(credit_interest)
    periods = math.ceil(
        math.log((monthly_payment
                  / (monthly_payment - i * credit_principal)), 1 + i))

    years = periods // 12
    months = periods % 12

    if months == 0:
        years_string = '1 year' if years == 1 else f'{years} years'
        print(f'You need {years_string} to repay this credit!')
    elif years == 0:
        months_string = '1 month' if months == 1 else f'{months} months'
        print(f'You need {months_string} to repay this credit!')
    else:
        years_string = '1 year' if years == 1 else f'{years} years'
        months_string = '1 month' if months == 1 else f'{months} months'
        print(f'You need {years_string} and {months_string} to repay this credit!')


def count_monthly_payment(credit_principal, periods, credit_interest):
    i = get_nominal_interest(credit_interest)
    pow_result = math.pow(1 + i, periods)

    monthly_payment = math.ceil(
        credit_principal * ((i * pow_result) / (pow_result - 1)))

    print(f'Your annuity payment = {monthly_payment}!')


def count_credit_principal(monthly_payment, periods, credit_interest):
    i = get_nominal_interest(credit_interest)
    pow_result = math.pow(1 + i, periods)

    credit_principal = round(
        monthly_payment / ((i * pow_result) / (pow_result - 1)))

    print(f'Your credit principal = {credit_principal}!')


def get_nominal_interest(credit_interest):
    return credit_interest / (12 * 100)


credit_calculator()
