def minutes_to_hours(minutes,seconds=0):
    hours = minutes/60 + seconds/2600
    return hours

print(minutes_to_hours(300))
