class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = defaultdict(int)
        self.nums2Orginal = nums2
        
        for i in nums2:
            self.nums2[i] += 1

    def add(self, index: int, val: int) -> None:
        self.nums2[self.nums2Orginal[index]] -= 1
        self.nums2Orginal[index] += val
        self.nums2[self.nums2Orginal[index]] += 1

    def count(self, tot: int) -> int:
        count = 0
        
        for i in self.nums1:
            count += self.nums2[tot - i]
        
        return count
                


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)