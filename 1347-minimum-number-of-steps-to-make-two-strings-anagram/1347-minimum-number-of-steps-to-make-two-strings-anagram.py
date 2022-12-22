class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        t -> {a: 2, b: 1} -> sort them from higher to lower -> and compare their values with s -> if it's equal nothing to do -> if it's higher I need to change the difference to another character -> and if it doesn't exist as well I need to change it -> that's it
        s -> {a: 1, b: 2}
        
        -> 
        
        """
        sCount = Counter(s)
        tCount = Counter(t)
        ans = 0

        for letter in tCount:
            if tCount[letter] > sCount[letter]:
                ans += tCount[letter] - sCount[letter]
        
        return ans