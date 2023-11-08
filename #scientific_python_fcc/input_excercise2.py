"""
Write a program to prompt the user for hours and
rate per hour using input to compute gross pay.
Use 35 hours and rate of 2.75 per hour to test
the program (ans 96.25). you should use input
to read a string and float to convert the string
to a number.
"""
hours_spent = input("Enter Hours: ")
rate_per_hour = input("Rate per hour($): ")
gross_pay = float(hours_spent) * float(rate_per_hour)
print(f"Payable amount = ${gross_pay}")

