from datetime import datetime, timedelta
import re
import time


def strptime_(date_str):
    """
    日期字符串转化为日期
    """
    separator = ''
    if '-' in date_str:
        separator = '-'
    elif '/' in date_str:
        separator = '/'
    return datetime.strptime(date_str, f'%Y{separator}%m{separator}%d')


def strftime_(date, separator = ''):
    """日期格式化为日期字符串"""
    return datetime.strftime(date, f'%Y{separator}%m{separator}%d')


def strftime_cn(date):
    return datetime.strftime(date, f'%Y年%m月%d日')


# date_str = str(20230331)
# date = strptime_(date_str)
# cn_date = strftime_cn(date)
# print(cn_date)
# print(f'{date.month}月{date.day}日')


# 时间戳
print(f'时间戳1：{time.time()}')
print(f'时间戳2：{int(datetime.now().timestamp())}')



def format_time(time, with_second=False, date=False):
    # '2023-03-08 15:00:06.180' -> '150006'
    arr = re.split('\s|:|\.', time)
    if date:
        return arr[0].replace('-','')
    if with_second:
        return int(arr[1]+arr[2]+arr[3])
    return int(arr[1]+arr[2])


print(format_time('2023-03-08 15:00:06.180', date=True))


# 日期
start = '2020-01-01'
total_year = int(datetime.now().year)-int(start.split('-')[0])
month = datetime.now().month
if month>6:
    total_year+=1
print(total_year)


"""获取星期几"""
print('获取星期几') 
def strptime_(date_str):
    """
    日期字符串转化为日期
    """
    separator = ''
    if '-' in date_str:
        separator = '-'
    elif '/' in date_str:
        separator = '/'
    return datetime.strptime(date_str, f'%Y{separator}%m{separator}%d')

def get_week(date_str, is_cn = False):
    """
    日期字符串获取星期几
    is_cn: 是否返回中文
    """
    date = strptime_(date_str)
    week = date.weekday()+1
    if is_cn:
        match week:
            case 1:
                week = '星期一'
            case 2:
                week = '星期二'
            case 3:
                week = '星期三'
            case 4:
                week = '星期四'
            case 5:
                week = '星期五'
            case 6:
                week = '星期六'
            case 7:
                week = '星期日'
    return week

day = '20230421'
print(f'{day}是星期几:{get_week(day)}')


"""时间差"""
time1 = datetime.now()
time.sleep(5)
time2 = datetime.now()
duration = time2-time1
print('时间差', duration.seconds)


print(datetime.now().strftime(f'%m%d.%H%M.%S'))

print('最新月：', datetime.today().month)
print('最新日期：', datetime.today().day)


def day_add(date, number):
    if isinstance(date, str):
        date = strptime_(date)
    return date + timedelta(days=number)

date = day_add(str(20230701), 1)
print(date.day)

today_week = datetime.now().weekday()
print('今天是星期几:', today_week+1)