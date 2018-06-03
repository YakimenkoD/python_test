from datetime import date
from dateutil.relativedelta import relativedelta

b_day = date(1996, 2, 29) 
i_day = date(2020, 3, 13)

def passport_validation(birth,issued):
	age = relativedelta(birth,date.today())
	print(age)
	if age in range(14,21):
		first_day_valid = birth + relativedelta(year)