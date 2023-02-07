class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr = [0, 0]
        North = (0, 1)
        South = (0, -1)
        East = (1, 0)
        West = (-1, 0)
        direction = North
        rotate = {
            'L': {
                North: West,
                West: South,
                South: East,
                East: North,
            },
            'R': {
                North: East,
                East: South,
                South: West,
                West: North
            }
        }
        
        
        for letter in instructions:
            if letter == 'G':
                curr[0] += direction[0]
                curr[1] += direction[1]
            else:
                direction = rotate[letter][direction]
        
        return direction != North or curr == [0, 0]