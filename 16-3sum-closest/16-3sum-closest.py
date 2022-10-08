class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        The brute force would be n ^ 3
        
        select my first number and try to find two numbers for it using in O(n) -> O(n ^ 2)
        
        i find the two numbers I will just use two numbers and move accordingly
        
        [-4, -1, 1, 2]
                 s  t
                 f
          ans = 2
        """
        ans = float('inf')
        nums.sort()
        
        temp=sum(nums[:3])
        if temp>target:
            return temp
        temp=sum(nums[-3:])
        if temp<target:
            return temp
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currAns = nums[i] + nums[left] + nums[right]

                if currAns == target:
                    return currAns
                elif currAns < target:
                    left += 1
                else:
                    right -= 1
                
                if abs(currAns - target) < abs(ans - target):
                    ans = currAns
                
        return ans