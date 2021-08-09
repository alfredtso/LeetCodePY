from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in nums[i+1:]:
                if tmp != nums[i]:
                    return [i, nums.index(tmp)]
                else:
                    ls = list(nums)
                    ls.remove(nums[i])
                    return [i, ls.index(tmp)+1]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, x in enumerate(nums):
            tmp = target - x
            # work because we can match it later on the second value
            if tmp not in map:
                map[x] = i
            else:
                return [map[tmp], i]




    def test(self):
        assert self.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
        assert self.twoSum(nums=[3, 3], target=6) == [0, 1]
        assert self.twoSum1(nums=[2, 7, 11, 15], target=9) == [0, 1]
        assert self.twoSum1(nums=[3, 3], target=6) == [0, 1]


if __name__ == '__main__':
    my = Solution()
    my.test()
