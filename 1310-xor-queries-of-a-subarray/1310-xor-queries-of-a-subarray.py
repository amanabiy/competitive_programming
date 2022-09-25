class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixOr = [0]
        ans = []

        for i in arr:
            prefixOr.append(i ^ prefixOr[-1])

        for left, right in queries:
            total = prefixOr[right + 1]
            previous = prefixOr[left]

            ans.append(total ^ previous)

        return ans