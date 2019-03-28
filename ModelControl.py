import datetime
import hello


def trim_date(date):
	return date.strftime('%Y-%m-%d')
	
#x = datetime.datetime.today().strftime('%Y-%m-%d')
y = datetime.datetime.today()
x = trim_date(y)
print(x)

t = datetime.date(2019, 1, 19)
d = trim_date(t)

print(d) 

if __name__ == "__main__":
	today = datetime.datetime.today()
	today = trim_date(today)
	schedule = hello.ScheduleObject(today)
	print(schedule.games_list)
 
 
