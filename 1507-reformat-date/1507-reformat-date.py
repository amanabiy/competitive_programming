class Solution:
    def reformatDate(self, date: str) -> str:
        monthName = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day, month, year = date.split()
        day = int(day[:-2])
        month = monthName.index(month) + 1
        
        return f'{year}-{month:02d}-{day:02d}'
    
        