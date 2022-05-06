class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for letter in s:
            if not stack or letter != stack[-1][0]:
                stack.append([letter, 1])
            else:
                if stack[-1][1] < k - 1:
                    stack[-1][1] += 1
                else:
                    stack.pop()
        return "".join([j * i for j, i in stack])