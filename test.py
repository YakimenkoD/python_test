from datetime import date, timedelta

b_day = date(1996, 2, 29) 
i_day = date(2018, 3, 13)

def passport_validation(birth,issued):
	age = (date.today() - birth) // timedelta(days=365.2425)
	if age in range(14,21):
		try:
			first_day_valid = birth.replace(year=birth.year + 14)
		except ValueError:
			first_day_valid = birth.replace(year=birth.year + 14, month=birth.month+1, day=1)
		last_day_valid  = birth.replace(year=birth.year + 20, month= birth.month+1)

		result = first_day_valid<=issued<=last_day_valid 

	elif age in range(20,46):
		try:
			first_day_valid = birth.replace(year=birth.year + 20)
		except ValueError:
			first_day_valid = birth.replace(year=birth.year + 20, month=birth.month+1, day=1)

		last_day_valid  = birth.replace(year=birth.year + 45, month= birth.month+1)
		result = first_day_valid <= issued <= last_day_valid
	
	elif age >=45:
		try:
			first_day_valid = birth.replace(year=birth.year + 45)
		except ValueError:
			first_day_valid = birth.replace(year=birth.year + 45, month=birth.month+1, day=1)

		result = first_day_valid<=issued 

	else:
		result = False
	return result if date.today()>=issued else False

print(passport_validation(b_day,i_day))
