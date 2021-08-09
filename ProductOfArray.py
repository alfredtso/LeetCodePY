"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of
all the elements of nums except nums[i].

>>>
"""
import collections
import numpy as np
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

       Must write algo runs in linear time

       :param nums:
       :return:

       >>> my = Solution()
       >>> my.productExceptSelf([1, 2, 3, 4])
       [24, 12, 8, 6]
       >>> my.productExceptSelf([-1,1,0,-3,3])
       [0, 0, 9, 0, 0]
       """

        ar = np.array(nums)
        res = np.array([1] * len(nums))

        for _ in range(len(nums)-1):
            # possibly expensive
            ar = np.roll(ar, 1)
            res *= ar

        return list(res)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
