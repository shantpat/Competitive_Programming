def convert_to_minutes(time):
    if time == '12:00 AM':
        minutes = 0
    elif time == '12:00 PM':
        minutes = 12*60
    else:
        t, ap = time.split(' ')
        h, m = t.split(':')
        minutes = int(h)*60 + int(m)
        if ap == 'AM' and h == '12':
            minutes -= 12*60
        if ap == 'PM' and h != '12':
            minutes += 12*60
    return minutes
print(convert_to_minutes('12:05 PM'))