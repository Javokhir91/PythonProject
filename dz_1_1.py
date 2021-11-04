duration = int(input('Введите желаемое число: '))

time_sec = duration % 60
time_min = duration % 3600 // 60
time_hour = duration % 86400 // 3600
time_day = duration // 86400

if duration < 0:
    print('Введите число больше нуля')
elif duration >=0 and duration <60:
    print(duration , 'сек')
elif duration >= 60 and duration < 3600:
    print(time_min, 'мин', time_sec, 'сек')
elif duration >=3600 and duration < 86400:
    print(time_hour, 'час', time_min, 'мин', time_sec, 'сек')
else:
    print(time_day, 'день', time_hour, 'час', time_min, 'мин', time_sec, 'сек')