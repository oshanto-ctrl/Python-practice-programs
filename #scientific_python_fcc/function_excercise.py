"""
Rewrite your pay computation with time-and-a-half
for overtime and create a function called
computepay() which takes two parameters(hours, rate)
"""

def computepay(hours, rate):
	
	try:
		hours_float = float(hours)
		rate_float = float(rate)
	except:
		print("Error! Please enter hour or rate as a number.")
		quit()

	if hours_float > 40.0:
		gross_pay = hours_float * rate_float
		overtime_pay = (hours_float - 40.0) * (rate_float * 1.5)
		gross_pay = gross_pay + overtime_pay
		return gross_pay
	else:
		gross_pay = hours_float * rate_float
		return gross_pay



# driver
hours = input("Enter Hours: ")
rate = input("Rate per hour($): ")
if float(hours) > 40.0:
	pay = computepay(hours, rate)
	print(f"Pay (Overtime Incluced) = ${pay}")
else:
	pay = computepay(hours, rate)
	print(f"Pay (Regular) = ${pay}")


# Finish

