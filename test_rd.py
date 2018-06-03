from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

b_day = date(1994, 6, 13) 
i_day = date(2016, 7, 28)

def passport_validation(birth,issued):
	age = (date.today() - birth) // timedelta(days=365.2425)
	if age in range(14,21):
		first_day_valid = birth + relativedelta(years=14)
		last_day_valid = birth + relativedelta(years=20, months=1)
		result = (first_day_valid<=issued<=last_day_valid) 

	elif age in range(20,46):
		first_day_valid = birth + relativedelta(years=20)
		last_day_valid = birth + relativedelta(years=45, months=1)
		result = (first_day_valid<=issued<=last_day_valid)

	elif age >=45:
		first_day_valid = birth + relativedelta(years=20)
		result = (first_day_valid<=issued) 

	return result if date.today()>=issued else False

print(passport_validation(b_day,i_day))