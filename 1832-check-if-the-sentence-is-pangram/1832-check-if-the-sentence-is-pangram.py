class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        nums = 0
        a = ord('a')
        for char in sentence:
            nums |= 1 << (ord(char) - a + 1)
        
        for i in range(1, 27):
            if not (nums & 1 << i):
                return False
        
        return True