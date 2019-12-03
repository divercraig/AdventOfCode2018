import re
import datetime
from day4.schedule import Schedule

events = {}
schedules = []
for line in open('input.txt'):
    timestamp_result = re.search('\[(.*)\](.*)', line)
    timestamp = timestamp_result.group(1)
    message = timestamp_result.group(2)
    time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    events[time] = message


current_schedule = None
sleep_start = None
sleep_end = None
guards = set()

for key in sorted(events):
    message = events[key]
    start_shift_result = re.search('Guard #(.*) begins shift', message)
    if start_shift_result:
        if current_schedule:
            schedules.append(current_schedule)
        current_schedule = Schedule(guard_id=int(start_shift_result.group(1)))
        guards.add(int(start_shift_result.group(1)))

    if "falls asleep" in message:
        current_schedule.set_date(month=key.month, day=key.day)
        sleep_start = key.minute

    if "wakes up" in message:
        sleep_end = key.minute
        current_schedule.add_snooze(start_minute=sleep_start, end_minute=sleep_end)

schedules.append(current_schedule)

worst_guard = (-1, -1, -1)  # id, minute, number of sleeps
for guard in guards:
    bad_minutes = {}
    for schedule in schedules:
        if schedule.guard_id == guard:
            for minute in schedule.midnight_hour_asleep.keys():
                if schedule.midnight_hour_asleep[minute]:
                    if minute not in bad_minutes.keys():
                        bad_minutes[minute] = 1
                    else:
                        bad_minutes[minute] = bad_minutes[minute] + 1

    worst_minute = (-1, -1)  # minute, number of sleeps
    for minute in bad_minutes.keys():
        if bad_minutes[minute] > worst_minute[1]:
            worst_minute = (minute, bad_minutes[minute])

    if worst_minute[1] > worst_guard[2]:
        worst_guard = (guard, worst_minute[0], worst_minute[1])

print("Worst guard is {}, at his worst at 00:{}".format(worst_guard[0], worst_guard[1]))
print("answer = {}".format(worst_guard[0] * worst_guard[1]))