class Solution:
    def racecar(self, target: int) -> int:
        """
        0 -> 1
        1 - 2 - 3
        3
        """
        pos = 0
        speed = 1
        step = 0

        startedFromHere = {}
        inQueue = {(pos, speed)}
        queue = deque([(pos, speed)])
        
        while queue:
            
            for _ in range(len(queue)):
                node, speed = queue.popleft()

                if node == target:
                    return step

                direction = 1 if speed < 0 else -1
                val = [(node + speed, speed * 2), (node, direction)]
                for position, s in val:
                    if (position, s) not in inQueue:
                        inQueue.add((position, s))
                        queue.append((position, s))
            
            step += 1
        
        return -1