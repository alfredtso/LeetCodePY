import math
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return a list of 1-indexed of the two number

        first_indx = 0
        last_indx = len(numbers) - 1

        # case 1: sum < target, check if mid + last > or < target
        # case 2: sum > target, check if first + mid >

        while first_indx < last_indx:

            result = numbers[first_indx] + numbers[last_indx] - target
            mid = math.floor((first_indx + last_indx) / 2)

            if result == 0:
                return [first_indx + 1, last_indx + 1]

            # case 1: if sum < target
            if result < 0:
                # we can see that the first num is in (first, mid]
                if numbers[mid] + numbers[last_indx] > target:
                    first_indx = first_indx + 1
                # reiterate from mid to last
                else:
                    first_indx = mid

            # case2: sum > target
            else:
                # one >, one <, we can deduct that the second num is in [mid,last)
                if numbers[first_indx] + numbers[mid] < target:
                    last_indx = last_indx - 1

                # reiterate from first to mid
                else:
                    last_indx = mid

    def test(self):
        assert self.twoSum([2, 3, 4], 6) == [1, 3]
        assert self.twoSum([-1, 0], -1) == [1, 2]
        assert self.twoSum([0, 0, 3, 4], 0) == [1, 2]
        assert self.twoSum([5, 25, 75], 100) == [2, 3]
        assert self.twoSum([3, 24, 50, 79, 88, 150, 345], 200) == [3, 6]


if __name__ == '__main__':
    my = Solution()
    my.test()
