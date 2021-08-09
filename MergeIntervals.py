from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        res = []

        for inter in intervals:
            if not res or res[-1][1] < inter[0]:
                res.append(inter)
            else:
                # e.g (1,5) and (1,4) merge to be (1,5)
                res[-1][1] = max(res[-1][1], inter[1])

        return res



    def test(self):
        assert self.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
        assert self.merge([[1,4],[4,5]]) == [[1,5]]

if __name__ == "__main__":
    my = Solution()
    my.test()
