def compund_interest(principal, rate, time):

    amount = principal * ((1+rate/100)**time)
    CI = amount - principal
    print("Compound interest is Rs.",CI)

principal = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

compund_interest(principal, rate, time)