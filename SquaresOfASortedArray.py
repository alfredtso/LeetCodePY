from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        >>> nums = [-4,-1,0,3,10]
        >>> Solution().sortedSquare(nums)
        [0, 1, 9, 16, 100]
        """
        # use builtin and listcomp
        return sorted([x * x for x in nums])

if __name__ == '__main__':
    import doctest
    doctest.testmod()

