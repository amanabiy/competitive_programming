class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        min_num = nums[k]
        curr_num = nums[k]
        
        left, right = k, k

        while right < len(nums) - 1 or left > 0:

            # if you have a choice select from one of them
            if right < len(nums) - 1 and left > 0:
                if nums[right + 1] > nums[left - 1]:
                    right += 1
                    min_num = min(min_num, nums[right])
                else:
                    left -= 1
                    min_num = min(min_num, nums[left])

            # if reached one end expand to the other
            elif right < len(nums) - 1:
                right += 1
                min_num = min(min_num, nums[right])
            else:
                left -= 1
                min_num = min(min_num, nums[left])
            
            curr_num = max(curr_num, min_num * (right - left + 1))
        
        return curr_num
                