import itertools
from typing import List
import math


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        lsofls = []
        lastnum = math.inf

        # less than 3 elm return []
        if len(nums) < 3:
            return lsofls

        # Sorted first as
        nums.sort()

        # for loop i and then use twosum
        for i in range(len(nums)):

            # Impossible case because the list was sorted
            if nums[i] > 0:
                break

            # Other cases, skip it, helper refers to the TwoSum solution
            if nums[i] != lastnum:
                self.helper(nums[i+1:], -nums[i], lsofls)

            # skip when the number is same as last one
            lastnum = nums[i]

        # handle duplicate
        lsofls.sort()
        lsofls = list(lsofls for lsofls,_ in itertools.groupby(lsofls))

        return lsofls

    def helper(self, numbers: List[int], target: int, ls: List[List[int]]) -> List[int]:

        # return the number itself

        first_indx = 0
        last_indx = len(numbers) - 1

        # not guaranteed to have solution

        while first_indx < last_indx:

            result = numbers[first_indx] + numbers[last_indx] - target

            if result == 0:
                # ugly
                ls.append([-target, numbers[first_indx], numbers[last_indx]])

            # case 1: if sum < target
            if result < 0:
                first_indx += 1
            else:
                last_indx -= 1

        return ls

    def threeSumHashSet(self, nums: List[int]):
        res, dups = set(), set()
        seen = {}

        # loop the list, val1 as pivot element
        for i, val1 in enumerate(nums):

            # handle duplicates without sorting
            if val1 not in dups:
                dups.add(val1)

            # inner loop for finding two pair complements to the pivot element
            for j, val2 in enumerate(nums[i+1:]):
                target = - (val1 + val2)

        # Dont understand the rest, come back later
        return

    def test(self):
        assert self.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]) == [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4],
                                                                         [-3, 0, 3], [-3, 1, 2], [-2, -1, 3],
                                                                         [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]
        assert self.threeSum([]) == []
        assert self.threeSum([0]) == []
        assert self.threeSum([0,0,0]) == [[0,0,0]]
        assert self.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


if __name__ == '__main__':
    my = Solution()
    my.test()
