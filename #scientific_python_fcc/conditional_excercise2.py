#2
"""
Rewrite your pay program using try and except so that your program handles non-numeric input 
gracefully by printing a message and exiting the program.

sample:
hour: 20
rate: nine
out: Error, please enter numeric input
"""
hours = input("Enter Hours: ")
rate= input("Rate per hour($): ")

try:
	hours_float = float(hours)
	rate_float = float(rate)
except:
	print("Error! Please enter hour or rate as a number.")
	# Quit program after this

if hours_float > 40.0:
	gross_pay = hours_float * rate_float
	overtime_pay = (hours_float - 40.0) * (rate_float * 1.5)
	print(f"Regular = ${gross_pay} Overtime = ${overtime_pay}")
	gross_pay = gross_pay + overtime_pay
	print(f"Pay (Overtime included) = ${gross_pay}")
else:
	gross_pay = hours_float * rate_float
	print(f"Pay (Regular) = ${gross_pay}")

