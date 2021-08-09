from typing import List
import collections


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ls = []
        counter = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for h in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[h] == target:
                            # check if already in ls using a separate counter list (improve later)
                            tmpls = [nums[i], nums[j], nums[k], nums[h]]
                            tmpc = collections.Counter(tmpls)
                            if tmpc not in counter:
                                counter.append(tmpc)
                                ls.append(tmpls)

        print(ls)
        return ls

    def test(self):
        assert self.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
        assert self.fourSum([0,0,0,0], 0) == [[0,0,0,0]]
        assert self.fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


if __name__ == '__main__':
    my = Solution()
    my.fourSum([1, 0, -1, 0, -2, 2], 0)
    my.fourSum([2, 2, 2, 2, 2], 8)
    my.test()
