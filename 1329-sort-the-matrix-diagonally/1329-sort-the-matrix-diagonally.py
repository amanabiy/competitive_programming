class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        count = defaultdict(list)
        arr = [ [ 0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                count[i - j].append(mat[i][j])
        
        for key in count.keys():
            count[key].sort(reverse=True)
            
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] = count[i - j].pop()
        
        return arr