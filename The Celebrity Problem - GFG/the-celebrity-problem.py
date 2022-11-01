#User function Template for python3
import sys
sys.setrecursionlimit(10**7)
class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, n, M):
        def dfs(person, graph, visited, famousPeople):
            countThePerson = 0
        
            for i, theyKnow in enumerate(graph[person]):
                if theyKnow == 1:
                    countThePerson += 1
                    if i not in visited:
                        visited.add(i)
                        dfs(i, graph, visited, famousPeople)
            
            if countThePerson == 0:
                famousPeople.add(person)

        famousPeople = set()
        visited = set()
        visited.add(0)
        dfs(0, n, visited, famousPeople)
        if len(famousPeople) == 1:
            # print(famousPeople)
            celebrity = famousPeople.pop()
            for i in range(len(n)):
                if i != celebrity and not n[i][celebrity]:
                    return -1
            return celebrity 
        else:
            return -1
        # code here 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends