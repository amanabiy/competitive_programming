from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.checkedIn = {}
        self.average = defaultdict(lambda: [0, 0]) # the [sum, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # add the person to the check In
        self.checkedIn[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkedIn[id]
        totalTime = t - startTime
        self.average[(startStation, stationName)][0] += totalTime
        self.average[(startStation, stationName)][1] += 1
        del self.checkedIn[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        identifier = (startStation, endStation)
        return self.average[identifier][0] / self.average[identifier][1]