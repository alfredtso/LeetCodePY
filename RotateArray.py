from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        
        >>> nums = [1,2,3,4,5,6,7]
        >>> k = 3
        >>> Solution().rotate(nums, k)
        [5, 6, 7, 1, 2, 3, 4]
        """
        length = len(nums)
        k %= length
        nums[:] = nums[length-k:] + nums[:length-k]
        # return nums[length-k:] + nums[:length-k]

    def rotate_2(self, nums: List[int], k: int):
        return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()


