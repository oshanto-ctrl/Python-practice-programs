#1
"""
Rewrite your pay computation to give the employee 
1.5 times the hourly rate for hours
worked above 40 hours.
"""
hours = input("Enter Hours: ")
rate= input("Rate per hour($): ")

hours_float = float(hours)
rate_float = float(rate)


if hours_float > 40.0:
	gross_pay = hours_float * rate_float
	overtime_pay = (hours_float - 40.0) * (rate_float * 1.5)
	print(f"Regular = ${gross_pay} Overtime = ${overtime_pay}")
	gross_pay = gross_pay + overtime_pay
	print(f"Pay (Overtime included) = ${gross_pay}")
else:
	gross_pay = hours_float * rate_float
	print(f"Pay (Regular) = ${gross_pay}")


