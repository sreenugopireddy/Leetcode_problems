class MyCalendarThree:

    def __init__(self):
        self.events = defaultdict(int)
        self.max_k = 0

    def book(self, startTime: int, endTime: int) -> int:

        self.events[startTime] += 1
        self.events[endTime] -= 1

        active = 0
        self.max_k = 0

        for time in sorted(self.events):
            active += self.events[time]
            self.max_k = max(self.max_k, active)

        return self.max_k

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)