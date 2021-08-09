"""Given an array of integers nums and an integer k, return the total number of
continuous subarrays whose sum equals to k.

# tag::SubarraySum

Test1::

    >>> my = Solution()
    >>> my.subarraySum([1,1,1], 2)
    2
    >>> my.subarraySum([1,2,3],3)
    2

# end::SubarraySum
"""

# tag::SubarraySum
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:

        # insert key 0 for the array from starting position
        map = defaultdict(int, {0: 1})
        csum = 0
        count = 0

        for x in nums:

            # get cumulative sum for the present position
            csum += x

            # increment count
            if csum - target in map.keys():
                count += map[csum - target]

            # insert cumulative sum
            map[csum] += 1

        return count


# end::SubarraySum

if __name__ == "__main__":
    import doctest

    doctest.testmod()
