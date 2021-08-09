from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        value_of_current_array = max_number_so_fast = nums[0]

        for x in nums[1:]:

            # discard the previous if adding new become smaller than the new itself
            value_of_current_array = max(x, value_of_current_array+x)
            max_number_so_fast = max(max_number_so_fast, value_of_current_array)

        return max_number_so_fast


    def maxSubArray1(self, nums: List[int]) -> int:
        # Note: when the subarray added up to negative can discard
        def helper(self, left, right):
            # choose left
            mid = (left + right) // 2

            # base case
            if left == right:
                return nums[left]

            # recursive: if negative only return left,
            # if positive return both
            right = helper(mid+1, right)
            left = helper(left, mid)

            if right + left > 0:
                return right + left


            return helper(left, mid) + helper(mid+1, right)

        return helper(0, len(nums) - 1)

    def test(self):
        assert self.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
        assert self.maxSubArray([5, 4, -1, 7, 8]) == 23




if __name__ == "__main__":
    my = Solution()
    my.test()
