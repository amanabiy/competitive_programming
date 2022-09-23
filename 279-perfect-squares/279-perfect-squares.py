from queue import Queue

class Solution:
    """
    Queue based solution
    """
    def numSquares(self, n: int) -> int:
        queue = Queue()
        visited = set()
        depth = -1

        queue.put(n)
        visited.add(n)
        while not queue.empty():
            depth += 1
            for _ in range(0, queue.qsize()):
                # pop the element and push 
                elem = queue.get()
                if elem == 0: 
                    return depth
                for i in range(1, math.floor(math.sqrt(elem))+1):
                    if elem - i*i not in visited:
                        queue.put(elem - i*i)
                        visited.add(elem-i*i)