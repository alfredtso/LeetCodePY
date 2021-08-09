import collections
import copy
import sys
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        """
        >>> sol = Solution()
        >>> candidates = [1,2]
        >>> target = 4
        >>> sol.combinationSum(candidates, target)
        [[1,1,1,1],[1,1,2],[2,2]]
        >>> candidates = [2,3,5]
        >>> target = 8
        >>> sol.combinationSum(candidates, target)
        [[2,2,2,2],[2,3,3],[3,5]]
        >>> candidates = [2,3,6,7]
        >>> target = 7
        >>> sol.combinationSum(candidates, target)
        [[2,2,3],[7]]
        >>> candidates = [2]
        >>> target = 1
        >>> sol.combinationSum(candidates, target)
        []
        >>> candidates = [1]
        >>> target = 1
        >>> sol.combinationSum(candidates, target)
        [[1]]
        >>> candidates = [1]
        >>> target = 2
        >>> sol.combinationSum(candidates, target)
        [[1,1]]

        :param candidates:
        :param target:
        :return:
        """

        combination = []

        def backtrack(target, path, start):

            if target == 0:
                combination.append(list(path))
                return
            elif target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                import pdb; pdb.set_trace()
                backtrack(target-candidates[i], path, i)
                path.pop()

        backtrack(target, [], 0)

        return combination

if __name__ == "__main__":
    import doctest
    doctest.testmod()