class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustGraph = defaultdict(list)
        reverseGraph = defaultdict(list)

        for a, b in trust:
            trustGraph[a].append(b)
            reverseGraph[b].append(a)
    
        for i in range(1, n + 1):
            if len(trustGraph[i]) == 0 and len(reverseGraph[i]) == n - 1:
                return i
        
        return -1