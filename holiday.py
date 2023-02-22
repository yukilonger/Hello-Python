import chinese_calendar
import datetime
import pandas as pd 

start_time = datetime.date(2023, 1, 1)  # 指定开始时间
end_time = datetime.date(2023, 12, 31)   # 指定结束时间

def xfor(days):
    result = ''
    for i,day in enumerate(days):
        result += f'{day[0]}\n'
    return result.strip('\n')


def xwrite(file_name, data):
    with open(file_name, 'w') as f:
        f.writelines(data)


workdays = pd.DataFrame(chinese_calendar.get_workdays(start_time,end_time))
xwrite('workday', xfor(workdays.values))

holidays = pd.DataFrame(chinese_calendar.get_holidays(start_time,end_time))
xwrite('dayoff', xfor(holidays.values))

print(f'total days count:{len(workdays.values)+len(holidays.values)}')