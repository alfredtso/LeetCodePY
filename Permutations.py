import collections
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        >>> sol = Solution()
        >>> nums = [1,2,3]
        >>> sol.permute(nums)
        [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        >>> nums = [0,1]
        >>> sol.permute(nums)
        [[0,1],[1,0]]
        >>> nums = [1]
        >>> sol.permute(nums)
        [[1]]

        :param nums:
        :return:
        """
        # nums all unique
        nums_set = set(nums)
        global permutation
        permutation = []
        d = collections.OrderedDict()

        self.backtrack(0, d, nums_set)
        return permutation

    def backtrack(self, index, path, nums_set):

        if index == len(nums_set):
            permutation.append([x for x in path.keys()])
            return

        candidates = self.construct_candidates(path, nums_set)

        for c in candidates:
            # add to path
            path[c] = None
            self.backtrack(index + 1, path, nums_set)
            path.popitem()

    def construct_candidates(self, path, nums_set):
        return nums_set - path.keys()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
