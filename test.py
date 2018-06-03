from datetime import date

b_day = date(2000, 2, 29)
i_day = date(2014, 3, 13)

def calculate_age(born):
    today = date.today()
    birthday = born.replace(year=today.year)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

def passport_validation(birth,issued):
	age = calculate_age(b_day)

	if age in range(14,21):
		first_day_valid = birth.replace(year=birth.year + 14)
		last_day_valid  = birth.replace(year=birth.year + 20, month= birth.month+1)
		return print(first_day_valid<=issued<=last_day_valid)

	elif age in range(20,46):
		first_day_valid = birth.replace(year=birth.year + 20)
		last_day_valid  = birth.replace(year=birth.year + 45, month= birth.month+1)
		return print(first_day_valid<=issued<=last_day_valid)

	elif age >=45:
		first_day_valid = birth.replace(year=birth.year + 45)
		return print(first_day_valid<=issued)

	else:
		return print(False)

passport_validation(b_day,i_day)


	