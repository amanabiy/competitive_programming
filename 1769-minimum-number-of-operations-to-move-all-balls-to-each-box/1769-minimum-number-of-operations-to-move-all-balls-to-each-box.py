class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        boxes = "110"
        """
        forward = [0]
        backward = [0]
        boxes = [int(x) for x in boxes]
        n = len(boxes)
        count = 0

        # forward 
        for i in range(1, n):
            count += boxes[i - 1]
            forward.append(forward[-1] + count)
        
        count = 0
        for i in range(n - 2, -1, -1):
            count += boxes[i + 1]
            backward.append(backward[-1] + (count))
        
        backward = list(reversed(backward))
        return [forward[i] + backward[i] for i in range(n)]            
                