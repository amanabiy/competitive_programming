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
        pos = {}
        ans = 0
        n = len(s)

        for i in range(n):
            if s[i] not in pos:
                pos[s[i]] = [i, i]
                continue
            pos[s[i]][1] = i
        
        for key in pos:
            left = pos[key][0] + 1
            right = pos[key][1]
            ans += len(set(list(s[left:right])))
        
        return ans