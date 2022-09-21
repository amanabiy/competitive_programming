class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        [1,2,3,4]
        []
        """
        sumEven = 0
        allQueriesEven = []
        for num in nums:
            if num % 2 == 0:
                sumEven += num
        
        for val, i in queries:
            newVal = nums[i] + val
            if newVal % 2 == 0:
                if nums[i] % 2 == 0:
                    sumEven += val
                else:
                    sumEven += newVal
            else:
                if nums[i] % 2 == 0:
                    sumEven -= nums[i]
            
            nums[i] = nums[i] + val   
            allQueriesEven.append(sumEven)
        
        return allQueriesEven