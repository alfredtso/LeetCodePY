"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

"""
import heapq
import itertools
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        result = self.method1(nums, k)

        return result

    def method1(self, nums: List[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> nums = [3,2,1,5,6,4]
        >>> k = 2
        >>> s.method1(nums, k)
        5
        >>> nums = [3,2,3,1,2,4,5,5,6]
        >>> k = 4
        >>> s.method1(nums, k)
        4

        :param nums:
        :param k:
        :return:
        """
        nums.sort()

        return nums[-k]

    def method2(self, nums: List[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> nums = [3,2,1,5,6,4]
        >>> k = 2
        >>> s.method2(nums, k)
        5
        >>> nums = [3,2,3,1,2,4,5,5,6]
        >>> k = 4
        >>> s.method2(nums, k)
        4

        :param nums:
        :param k:
        :return:
        """
        h = []
        for x in nums:
            heapq.heappush(h, x)

        res = heapq.nlargest(k, h)

        return res[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()