import datetime


def seconds_to_formated_hours(seconds):
    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    minutes = minutes % 60

    result = ""
    if hours != 0:
        result += f"{hours}h"
    if minutes != 0:
        result += f"{minutes}m"
    return result

def str_to_date_tuple(input):
    now = datetime.datetime.now()
    day = now.day
    month = now.month
    year = now.year

    spplited = input.split('/')

    if len(spplited) >= 1:
        day = int(spplited[0])
    
    if len(spplited) == 2:
        if(int(spplited[1]) > 12):
            day = -1
            month = int(spplited[0])
            year = int(spplited[1])
        else:
            month = int(spplited[1])
    elif len(spplited) == 3:
        month = int(spplited[1])
        year = int(spplited[2])

    return (day, month, year)

def tuple_to_datestring(input):
    day, month, year = input
    result_date = datetime.date(year, month, day)
    return str(result_date)

def last_day_of_month(any_date):
    # this will never fail
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = any_date.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)
    

if __name__ == "__main__":
    dates = ["05", "08/2021", "03/05", "15/04/2021"]
    tuppled_dates = []

    for date in dates:
        result = str_to_date_tuple(date)
        if result[0] == -1:
            (day, month, year) = result
            result = (1, month, year)
        tuppled_dates.append(result)

    for tuppled_date in tuppled_dates:
        print(tuple_to_datestring(tuppled_date))



