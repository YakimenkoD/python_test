from datetime import date, timedelta

b_day = date(2018, 6, 4) 
i_day = date(2020, 3, 13)



def passport_validation(birth,issued):
	age = (date.today() - birth) // timedelta(days=365.2425)
	if age in range(14,21):
		try:
			first_day_valid = birth.replace(year=birth.year + 14)
		except ValueError:
			first_day_valid = birth.replace(year=birth.year + 14, month=birth.month+1, day=1)
		
		try:
			last_day_valid  = birth.replace(year=birth.year + 20, month= birth.month+1)
		except ValueError:
			last_day_valid  = birth.replace(year=birth.year + 20, month= birth.month+1,day=1)

		return first_day_valid<=issued<=last_day_valid

	elif age in range(20,46):
		try:
			first_day_valid = birth.replace(year=birth.year + 20)
		except ValueError:
			first_day_valid = birth.replace(year=birth.year + 20, month=birth.month+1, day=1)
		
		try:
			last_day_valid  = birth.replace(year=birth.year + 45, month= birth.month+1)
		except ValueError:
			last_day_valid  = birth.replace(year=birth.year + 45, month= birth.month+1, day=1)

		return first_day_valid <= issued <= last_day_valid
	
	elif age >=45:
		try:
			first_day_valid = birth.replace(year=birth.year + 45)
		except ValueError:
			first_day_valid = birth.replace(year=birth.year + 45, month=birth.month+1, day=1)

		return first_day_valid<=issued

	else:
		return False

print(passport_validation(b_day,i_day))


'''def calculate_age(born):
    today = date.today()
    try: 
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year'''