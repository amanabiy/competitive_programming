class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        ans = [-1] * len(nums)
        graph = defaultdict(list)
        
        for frm, to in edges:
            graph[frm].append(to)
            graph[to].append(frm)
        
        def dfs(node, parent, seen, depth=0):
            d = -1
            for elems in seen:
                if gcd(nums[node], elems) == 1 and seen[elems]:
                    if d < seen[elems][-1][1]:
                        ans[node] = seen[elems][-1][0]
                        d = seen[elems][-1][1]

            seen[nums[node]].append([node, depth])    
            for child in graph[node]:
                if child != parent:
                    dfs(child, node, seen, depth + 1)
            seen[nums[node]].pop()

        if edges:
            dfs(0, -1, defaultdict(list))
        return ans