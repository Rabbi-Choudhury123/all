def simple_interest(p,r,t):
    print('The principal is', p)
    print('The interest rate is ', r)
    print('The time period is ',t)

    si = (p * t * r)/100

    print('The simple interest is', si)
    return si

p = float(input("Enter the Principal amouont"))
r = float(input("Enter the rate of interest"))
t = float(input("Enter the time period"))
simple_interest(p,r,t)