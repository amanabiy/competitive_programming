class Solution:
    def hasExpectedOnes(self, num, numOnes):
        count = 0
        
        for i in range(32):
            if num & (1 << i):
                count += 1
        
        return count

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = []
        minutes = []
        ans = []
        
        for i in range(60):
            countOnes = self.hasExpectedOnes(i, turnedOn)
            if countOnes <= turnedOn:
                if i < 12:
                    hours.append([i, countOnes])
                minutes.append([i, countOnes])

        for hour, countOnes in hours:
            for minute, countOneMin in minutes:
                if countOnes + countOneMin == turnedOn:
                    minut = str(minute) if minute > 9 else "0" + str(minute)
                    ans.append( str(hour) + ":" + minut)
        
        return ans