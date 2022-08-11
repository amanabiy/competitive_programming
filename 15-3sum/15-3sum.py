class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        calculated = set()
        nums.sort()
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            
            if nums[i] not in calculated:
                
                while left < right:
                    three_sum = nums[left] + nums[right] + nums[i]
                    
                    if three_sum == 0 and (nums[left], nums[right]) not in calculated:
                        ans.append([nums[i], nums[left], nums[right]])
                        calculated.add((nums[left], nums[right]))
                        left += 1
                        right -= 1
                
                    elif three_sum <= 0:
                        left += 1
                    else:
                        right -= 1
        

            calculated.add(nums[i])

        return ans