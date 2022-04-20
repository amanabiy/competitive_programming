class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = [ i for i in range(len(accounts)) ]
        emails = {}
        ans = defaultdict(list)
        rank = [1] * len(accounts)
        
        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1,node2):
            par1 = find(node1)
            par2 = find(node2)
            
            if par1 != par2:
                if rank[par1] > rank[par2]:
                    parents[par2] = par1
                    rank[par1] += rank[par2]
                elif rank[par2] >= rank[par1]:
                    parents[par1] = par2
                    rank[par2] += rank[par1]

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in emails:
                    union(i, emails[accounts[i][j]])
                emails[accounts[i][j]] = i

        for key in emails.keys():
            person = find(emails[key])
            ans[person].append(key)
            
        return [[accounts[key][0]] + sorted(value) for key, value in ans.items()]
        