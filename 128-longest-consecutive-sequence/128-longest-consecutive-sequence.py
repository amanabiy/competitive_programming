class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {i:i for i in nums}
        rank = {i:1 for i in nums}
        
        def find(nd):
            if nd == parent[nd]:
                return nd
            parent[nd] = find(parent[nd])
            return parent[nd]
        
        def union(num1, num2):
            p1, p2 = find(num1), find(num2)
            
            if p1 != p2:
                if rank[p1] >= rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
        
        for num in nums:
            if num - 1 in parent:
                union(num - 1, num)
            if num + 1 in parent:
                union(num + 1, num)

        return max(rank.values()) if rank else 0