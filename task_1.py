seconds = int(input('Введите временной промежуток: '))
duration = seconds
minutes = seconds // 60
hours = minutes // 60
days = hours // 24

if seconds <= 60:
    print('duration =', duration)
    print(seconds, 'sec')
elif seconds > 60 > minutes and hours < 24:
    seconds = seconds % 60
    print('duration =', duration)
    print(minutes, 'min', seconds, 'sec' )
elif minutes >= 60 and seconds > 60 and hours < 24:
    seconds = seconds % 60
    minutes = minutes % 60
    print('duration =', duration)
    print(hours, 'h', minutes, 'min', seconds, 'sec')
elif minutes >= 60 and seconds > 60 and hours >= 24:
    seconds = seconds % 60
    hours = hours % 24
    minutes = minutes % 60
    print('duration =', duration)
    print(days, 'd', hours, 'h', minutes, 'min', seconds, 'sec')

