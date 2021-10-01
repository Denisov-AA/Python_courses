import datetime


def working_day_in_period(f_start_date, f_end_date):
    day_delta = datetime.timedelta(days=1)
    current_day = f_start_date
    working_days = 0
    for day in range((f_end_date - f_start_date).days):
        if datetime.datetime.weekday(current_day) != 5:
            if datetime.datetime.weekday(current_day) != 6:
                working_days += 1
        current_day += day_delta

    return working_days


input_start_date = input("Input start date: DD-MM-YYYY\n").strip().split('.')
input_end_date = input("Input start date: DD-MM-YYYY\n").strip().split('.')

try:
    start_date = datetime.datetime(int(input_start_date[2]), int(input_start_date[1]), int(input_start_date[0]))
    end_date = datetime.datetime(int(input_end_date[2]), int(input_end_date[1]), int(input_end_date[0]))
except Exception:
    start_date = datetime.date.today()
    end_date = datetime.date.today()
    print("Wrong date format, try again")
print(f"Workig dates between dates: {working_day_in_period(start_date, end_date)}")
