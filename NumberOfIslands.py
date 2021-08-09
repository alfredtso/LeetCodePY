from typing import List
import sys


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        res = 0

        # brute force
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)

        return res

    def dfs(self, grid: List[List[str]], r, c):

        # get m and n
        m = len(grid)
        n = len(grid[0])

        # Stopping conditions
        if r < 0 or c < 0 or r > m or c > n or grid[r][c] == "0":
            return

        # trick: mark visited as 0
        grid[r][c] == "0"

        # recursion for 4 directions; use stopping conditions to screen out edge case
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)


    def test(self):
        assert self.numIslands([
            ["1", "0"],
            ["1", "0"]
        ]) == 1
        assert self.numIslands([
            ["1", "0"],
            ["0", "1"]
        ]) == 2
        assert self.numIslands([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]) == 3
        assert self.numIslands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]) == 1


if __name__ == "__main__":
    my = Solution()
    my.test()
