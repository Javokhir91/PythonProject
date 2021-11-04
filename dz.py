

duration = int(input('Введите желаемое число: '))
m =  60
hour =  3600
day =  86400
year = 31622400

timesec = duration % m
timemin = duration % hour // m
timehour = duration % day // hour
timeday = duration % year // day
timeyear = duration // year

if duration < 0:
    print('Введите число больше нуля')
elif duration >=0 and duration <m:
    print(duration , 'сек')
elif duration >= m and duration < hour:
    print(timemin, 'мин', timesec, 'сек')
elif duration >=hour and duration < day:
    print(timehour, 'час', timemin, 'мин', timesec, 'сек')
elif duration >= day and duration < year:
    print(timeday, 'день', timehour, 'час', timemin, 'мин', timesec, 'сек')
else:
    print(timeyear, 'год', timeday, 'день', timehour, 'час', timemin, 'мин', timesec, 'сек')
