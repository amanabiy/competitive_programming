class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        0123456789
        ADOBECODEBANC     ABC = 3
              l
                    r
         {
            A: 1
            B: 1
            C: 1
         }

         length = 3
        
        """
        letters = defaultdict(int)
        originalT = Counter(t)
        left = right = length = 0
        ans = ""
        
        while right < len(s) + 1 and left < len(s):
            # expanding to the right
            if length < len(t) and right < len(s):
                newLetter = s[right]
                if newLetter in originalT:
                    if letters[newLetter] < originalT[newLetter]:
                        length += 1
                    letters[newLetter] += 1
                right += 1
    
            # shirnking from left
            else:
                lastLetter = s[left]
                if lastLetter in originalT:
                    if letters[lastLetter] <= originalT[lastLetter]:
                        length -= 1
                    letters[lastLetter] -= 1
                left += 1

            if length == len(t):
                # print(ans, s[left:right], right - left)
                if ans == "" or len(ans) >= right - left:
                    ans = s[left:right]
            # print(left, right, length)
        return ans
        