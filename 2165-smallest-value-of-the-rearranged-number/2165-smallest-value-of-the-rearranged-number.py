class Solution:
    def smallestNumber(self, num: int) -> int:
        """
        Count the letters and add them accordingly
        """
        arr = [0 for i in range(10)]
        nums = str(num)
        ans = 0
        
        for i in nums:
            if i != '-':
                arr[int(i)] += 1
        
        if nums[0] == '-':
            for i in range(len(arr) - 1, -1, -1):
                if arr[i]:
                    ans = ans * (10 ** arr[i]) + int(f"{i}" * arr[i])
            ans *= -1
        else:
            zero_set = False
            for i in range(1, len(arr)):
                if  not zero_set:
                    if arr[i]:
                        ans += i
                        arr[i] -= 1
                        ans = ans * (10 ** arr[0])
                        zero_set = True
                    
                if arr[i]:
                    ans = ans * (10 ** arr[i]) + int(f"{i}" * arr[i])
                
            
        return ans
        