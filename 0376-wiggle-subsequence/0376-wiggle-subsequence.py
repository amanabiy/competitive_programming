class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return 1

        prevIsPositive = None 
        ans = [nums[0]]

        for i in range(1, len_nums):
            # lookinf for negative parity
            if prevIsPositive == None:
                if ans[-1] != nums[i]:
                    prevIsPositive = nums[i] - ans[-1] > 0 # True if have a positive parity
                    ans.append(nums[i])
            elif prevIsPositive:
                if ans[-1] > nums[i]:
                    ans.append(nums[i])
                    prevIsPositive = False
            else:
                if ans[-1] < nums[i]:
                    ans.append(nums[i])
                    prevIsPositive = True
            ans[-1] = nums[i]

        return len(ans)

