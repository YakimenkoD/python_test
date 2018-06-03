from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

b_day = date(2000, 2, 29) 
i_day = date(2020, 3, 13)

def passport_validation(birth,issued):
	age = (date.today() - birth) // timedelta(days=365.2425)
	if age in range(14,21):
		first_day_valid = birth + relativedelta(years=14)
		last_day_valid = birth + relativedelta(years=20, months=1)
		print(first_day_valid)
		print(last_day_valid)
		return (first_day_valid<=issued<=last_day_valid) if date.today()>=issued else False

print(passport_validation(b_day,i_day))