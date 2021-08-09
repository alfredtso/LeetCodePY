import copy
import math
from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0

        # last the last 2 as left and right below
        for i, num1 in enumerate(nums[:-2]):

            immedi_target = target - num1

            left, right = i + 1, len(nums) - 1

            while left < right:

                if nums[left] + nums[right] >= immedi_target:
                    right -= 1

                else:
                    result += (right - left)
                    left += 1
        return result



    def test(self):
        assert self.threeSumSmaller([-1,1,-1,-1], -1) == 1
        assert self.threeSumSmaller([3,1,0,-2], 4) == 3
        assert self.threeSumSmaller([-2, 0, 1, 3], 2) == 2
        assert self.threeSumSmaller([1,-2,2,1,0], 1) == 4


if __name__ == '__main__':
    my = Solution()
    my.test()
