class Schedule:

    def __init__(self, guard_id: int):
        self.guard_id = guard_id
        self.month = None
        self.day = None
        self.midnight_hour_asleep = {}
        for i in range(0, 60):
            self.midnight_hour_asleep[i] = False

    def set_date(self, month:int, day:int):
        self.month = month
        self.day = day

    def add_snooze(self, start_minute: int, end_minute):
        for i in range(start_minute, end_minute):
            self.midnight_hour_asleep[i] = True

    def length_of_naps(self):
        count = 0
        for minute_asleep in self.midnight_hour_asleep.values():
            if minute_asleep:
                count += 1
        return count
