class Solution:
    def numberToWords(self, num: int) -> str:
        """
        
        """
        if num == 0:
            return "Zero"

        oneToNineteen = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        
        
        
        nums = list(reversed(str(num)))
        ans = []
        start = 0
        hundreds = ['', 'Thousand', 'Million', 'Billion']
        
        
        for j in range(0, len(nums), 3):
            smallName = []
            n = nums[j:j+3][::-1]
            i = 0
            
            if len(n) == 3:
                if n[i] != "0":
                    smallName += [oneToNineteen[int(n[i]) - 1], 'Hundred']
                i += 1
            
            if len(n) >= 2 and int(n[i]) > 1:
                if n[i] != "0":
                    smallName += [tens[int(n[i]) - 2]]
                i += 1
            if n[i] == "0":
                i += 1
            x = None
            if i < len(n):
                x = n[i]        
            if  i + 1 < len(n) and len(n) >= 2 and int(n[i]) == 1:
                if x != "0":
                    x = n[i] + n[i + 1]
            if i < len(n) and len(n) >= 1:
                if x!= "0":
                    smallName += [oneToNineteen[int(x) - 1]]
                i += 1
            if smallName:
                smallName += [hundreds[start]]
            start += 1
            ans += list(reversed(smallName))
        
        return ' '.join(list(reversed(ans))).strip()
        
        
        
        
        