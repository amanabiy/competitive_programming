class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        index_add = bisect.bisect_left(self.booking, [start, end])
        
        
        # check the calendar to the left of the given index
        if index_add > 0:
            if self.booking[index_add - 1][1] > start or \
            start <= self.booking[index_add - 1][0] <= end :
                return False
        
        # check the calendar on the returned index(right)
        if index_add < len(self.booking):
            if self.booking[index_add][0] < end:
                return False
        
        self.booking.insert(index_add, [start, end])
        
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)