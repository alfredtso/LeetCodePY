import collections
import itertools


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 2 cases:
        # return to 0,0 after one cycle
        # or not facing north
        # clockwise 90 degrees +1
        direction = 0
        x = 0
        y = 0

        # x, y coordiantes delta according to direction
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # loop through instruction
        for instruction in instructions:
            if instruction == "R":
                direction = (direction + 1) % 4
            elif instruction == "L":
                direction = (direction + 3) % 4
            elif instruction == "G":
                x += delta[direction][0]
                y += delta[direction][1]

        # conclude
        return (x == 0 and y == 0) or direction != 0

    def test(self):
        assert self.isRobotBounded("GGLLGG") == True
        assert self.isRobotBounded("GG") == False
        assert self.isRobotBounded("GL") == True


if __name__ == "__main__":
    my = Solution()
    my.test()
