class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return 1

        prevIsPositive = None 
        ans = nums[0]
        count = 1

        for i in range(1, len_nums):

            # lookinf for negative parity
            if prevIsPositive == None:
                if ans != nums[i]:
                    prevIsPositive = nums[i] - ans > 0 # True if have a positive parity
                    count += 1
            elif prevIsPositive:
                if ans > nums[i]:
                    count += 1
                    prevIsPositive = False
            else:
                if ans < nums[i]:
                    count += 1
                    prevIsPositive = True
            ans = nums[i]

        return count

