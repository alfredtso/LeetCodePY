import itertools
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        # sort with both keys
        items.sort(key=lambda x: (x[0], -x[1]))

        res = []
        tmp = []
        for key, group in itertools.groupby(items, lambda x: x[0]):
            for i, val in enumerate(group):
                if i != 5:
                    tmp.append(val[1])

                # leave the inner loop when reach 5
                else:
                    break

            # append the result
            res.append([key, sum(tmp) // 5])

            # clear the tmp list
            tmp.clear()

        return res



    def test(self):
        assert self.highFive([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]) == [[1, 87], [2, 88]]
        assert self.highFive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]) == [[1, 100], [7, 100]]


if __name__ == "__main__":
    my = Solution()
    my.test()
