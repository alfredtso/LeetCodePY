import collections
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        >>> s = Solution()
        >>> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        >>> s.spiralOrder(matrix)
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        >>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
        >>> s.spiralOrder(matrix)
        [1, 2, 3, 6, 9, 8, 7, 4, 5]

        :param matrix:
        :return:
        """
        res = self.naive(matrix)

        return res

    def naive(self, matrix: List[List[int]]) -> List[int]:

        i = 0
        j = 0
        col = len(matrix[0])
        row = len(matrix)
        res = []
        # 0: Norther, 1:East etc
        direction = 1

        # limits
        x_direction = collections.deque(range(1,row))
        y_direction = collections.deque(range(col))

        while len(res) < col*row:
            if direction % 4 == 1:
            # direction 1: i: unchange, j++
                tmp = y_direction.pop()
                while j <= tmp:
                    res.append(matrix[i][j])
                    j += 1
                    # correct the last loop
                j -= 1
                direction += 1
                i += 1

            elif direction % 4 == 2:
                # i++ , j unchange
                tmp = x_direction.pop()
                while i <= tmp:
                    res.append(matrix[i][j])
                    i += 1

                i -= 1
                direction += 1
                j -= 1

            elif direction % 4 == 3:
                # i , j--
                tmp = y_direction.popleft()
                while j >= tmp:
                    res.append(matrix[i][j])
                    j -= 1
                j += 1
                direction += 1
                i -= 1

            elif direction % 4 == 0:
                # i--, j
                tmp = x_direction.popleft()
                while i >= tmp:
                    res.append(matrix[i][j])
                    i -= 1
                i += 1
                direction += 1
                j += 1

        return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()

