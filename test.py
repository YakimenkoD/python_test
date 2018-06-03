from datetime import date

b_day = date(2000, 2, 29)
i_day = date(2014, 3, 13)

def calculate_age(born):
    today = date.today()
    try: 
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

def passport_validation(birth,issued):
	age = calculate_age(b_day)

	if age in range(14,21):
		try:
			first_day_valid = birth.replace(year=birth.year + 14)
		except ValueError:
			first_day_valid = birth.replace(year=birth.year + 14, month=birth.month+1, day=1)
		
		try:
			last_day_valid  = birth.replace(year=birth.year + 20, month= birth.month+1)
		except ValueError:
			last_day_valid  = birth.replace(year=birth.year + 20, month= birth.month+2,day=1)

		return print(first_day_valid<=issued<=last_day_valid)

	elif age in range(20,46):
		try:
			first_day_valid = birth.replace(year=birth.year + 20)
		except ValueError:
			first_day_valid = birth.replace(year=birth.year + 20, month=birth.month+1, day=1)
		
		try:
			last_day_valid  = birth.replace(year=birth.year + 45, month= birth.month+1)
		except ValueError:
			last_day_valid  = birth.replace(year=birth.year + 45, month= birth.month+2,day=1)
	
	elif age >=45:
		try:
			first_day_valid = birth.replace(year=birth.year + 45)
		except ValueError:
			first_day_valid = birth.replace(year=birth.year + 45, month=birth.month+1, day=1)

		return print(first_day_valid<=issued)

	else:
		return print(False)

passport_validation(b_day,i_day)


	