class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        """
        tiles = [[1, 5], [10, 18], [24, 25], [30, 32]], carpetLen = 12
        
        starting =   [1,10,24,30]
        endings =    [5,18,25,32]
        tilesSum = [0,5,14,16,19]
        
        start from 10 and 10 + 12 - 1 = 21
        (24 - 25 + 1) the size at 24
        does 21 reach 24? no so 
        (so take only 14 - 5 == 9)
        
        
        starting =   [1,10,20,30]   carpetLen = 13
        endings =    [5,18,25,32]
        tilesSum = [0,5,14,16,19]
    
        the other condition would be:
        carpet starts from 10 and 10 + 13 - 1 = 22
        I will try to find the position where 22 is?
        (25 - 20 + 1) is the size at 20
        does 22 > 20 Yes: share a size of 22 - 20 + 1 = 3
        (so take only 14 - 5 + 3 == 12)

        """
        tiles.sort()
        
        prefix, start_indx = [0], []
        for i, j in tiles:
            start_indx.append(i)
            prefix.append(j - i + 1 + prefix[-1])
            
        ans = 0
        for i, elem in enumerate(tiles):
            u, v = elem
            length_to_cover = u + carpetLen - 1
            
            if v >= length_to_cover:
                return carpetLen
            
			# binary search applied here
            end_indx = bisect_right(start_indx, length_to_cover) - 1
            
            length_diff = 0
            if tiles[end_indx][1] > length_to_cover:
                length_diff = tiles[end_indx][1] - length_to_cover
            ans = max(ans, prefix[end_indx + 1] - prefix[i] - length_diff)
            

        return ans