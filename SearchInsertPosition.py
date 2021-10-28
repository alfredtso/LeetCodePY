from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the
        index if the target is found. If not, return the index where it would be
        if it were inserted in order.
        
        You must write an algorithm with O(log n) runtime complexity.

        >>> nums = [1,3,5,6]
        >>> target = 5
        >>> Solution().searchInsert(nums, target)
        2
        >>> nums = [1,3,5,6]
        >>> target = 2
        >>> Solution().searchInsert(nums, target)
        1
        >>> nums = [1,3,5,6]
        >>> target = 7
        >>> Solution().searchInsert(nums, target)
        4
        >>> nums = [1,3,5,6]
        >>> target = 0
        >>> Solution().searchInsert(nums, target)
        0
        >>> nums = [1]
        >>> target = 0
        >>> Solution().searchInsert(nums, target)
        0
        >>> nums = [1]
        >>> target = 1
        >>> Solution().searchInsert(nums, target)
        0
        """
        lo = 0
        hi = len(nums) - 1

        while lo < hi:

            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        #
        if target <= nums[lo]:
            return lo
        else:
            return lo + 1



if __name__ == '__main__':
    import doctest
    doctest.testmod()

