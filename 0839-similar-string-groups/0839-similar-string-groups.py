class Solution:
    def numSimilarGroups(self, anagrams: List[str]) -> int:
        parent = {}
        rank  = {}
        for i in range(len(anagrams)):
            parent[i] = i
            rank[i] = 1
        groups = len(anagrams)
        def find_parent(stra):
            if parent[stra] == stra:
                return stra
            parent[stra] = find_parent(parent[stra])
            return parent[stra]


        def union(stra, strb):
            pa = find_parent(stra)
            pb = find_parent(strb)

            if pa != pb:
                if rank[pa] >= rank[pb]:
                    parent[pb] = pa
                    rank[pa] += rank[pb]
                else:
                    parent[pa] = pb
                    rank[pb] += rank[pa]
                return True
            return False


        def check(stra, strb):
            count = 0
            for i in range(len(stra)):
                if stra[i] != strb[i]:
                    count += 1
            return True if count <= 2 else False


        for i in range(len(anagrams)):
            for j in range(i + 1,len(anagrams)):
                if check(anagrams[i], anagrams[j]) and union(i,j):
                    groups -= 1

        return groups