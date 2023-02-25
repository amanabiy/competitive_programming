class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        s = "aabca"
        
        - palindrome subsequence
        - length = 3
        - unique
        
        
        left and right
           [start, end]
        a: [0, 10^5] -> set(letters) -> unique
        b: [2, 10]
        
        Time
        count -> n
        skip if start == end or start + 1 == end
        inserttToSet -> (26 *  n) 
        
        Time: O(n)
        Space: O(1)
        
        Two pointer start right from the end
        0123456789 10
        aabcdefbcczzzz b   10
        l              r
        
        uniqueLettersBetween 0 and 8 -> b, c, d, e, f
        
        bcd  cdc dbd
        bdb  cbc dcd
        bab
        bbb
        
        26 *
               L     R
        Time:  n + (26 * n) -> O(n) (n -> length of the array)
        visited -> 26 , inMiddle -> 26
        Space: O(26) -> O(1)
        """
        visited = set()
        ans = 0
        n = len(s)

        for i in range(n):
            if s[i] not in visited:
                right = n - 1
                while right > i and s[right] != s[i]:
                    right -= 1
                visited.add(s[i])
                ans += len(set(list(s[i + 1:right])))
        
        return ans