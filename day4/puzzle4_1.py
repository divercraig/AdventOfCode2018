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
for key in sorted(events):
    message = events[key]
    start_shift_result = re.search('Guard #(.*) begins shift', message)
    if start_shift_result:
        if current_schedule:
            schedules.append(current_schedule)
        current_schedule = Schedule(guard_id=int(start_shift_result.group(1)))

    if "falls asleep" in message:
        current_schedule.set_date(month=key.month, day=key.day)
        sleep_start = key.minute

    if "wakes up" in message:
        sleep_end = key.minute
        current_schedule.add_snooze(start_minute=sleep_start, end_minute=sleep_end)

schedules.append(current_schedule)

guard_sleep_time = {}

for schedule in schedules:
    if schedule.guard_id in guard_sleep_time.keys():
        guard_sleep_time[schedule.guard_id] = guard_sleep_time[schedule.guard_id] + schedule.length_of_naps()
    else:
        guard_sleep_time[schedule.guard_id] = schedule.length_of_naps()

worst_guard = (-1, -1)
for guard_id in guard_sleep_time.keys():
    if guard_sleep_time[guard_id] > worst_guard[1]:
        worst_guard = (guard_id, guard_sleep_time[guard_id])

sleep_minutes = {}

for schedule in schedules:
    if schedule.guard_id == worst_guard[0]:
        for minute in schedule.midnight_hour_asleep.keys():
            if schedule.midnight_hour_asleep[minute]:
                if minute not in sleep_minutes.keys():
                    sleep_minutes[minute] = 1
                else:
                    sleep_minutes[minute] = sleep_minutes[minute] + 1

worst_minute = (-1, -1)

for minute in sleep_minutes.keys():
    if sleep_minutes[minute] > worst_minute[1]:
        worst_minute = (minute, sleep_minutes[minute])

print("Worst guard is {}, at his worst at 00:{}".format(worst_guard[0], worst_minute[0]))
print("answer = {}".format(worst_guard[0] * worst_minute[0]))
