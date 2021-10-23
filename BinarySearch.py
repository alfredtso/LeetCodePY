from typing import List
import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        >>> nums = [-1,0,3,5,9,12]
        >>> target = 9
        >>> Solution().search(nums, target)
        4
        >>> nums = [-1, 0, 3]
        >>> target = 2
        >>> Solution().search(nums, target)
        -1
        """
        head = 0
        tail = len(nums) - 1

        while (head <= tail):
            middle = head + (tail - head) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                tail = middle - 1
            else:
                head = middle + 1

        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
