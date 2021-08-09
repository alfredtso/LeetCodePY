import collections
import math
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        >>> sol = Solution()
        >>> n = 6
        >>> edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
        >>> sol.findMinHeightTrees(edges, n)
        [3, 4]
        >>> n = 1
        >>> edges = []
        >>> sol.findMinHeightTrees(edges, n)
        [0]
        >>> n = 2
        >>> edges = [[0,1]]
        >>> sol.findMinHeightTrees(edges, n)
        [0, 1]

        :param n:
        :param edges:
        :return:
        """
        length = [-1]* (n-1)



        for x in range(n):
            # for each x record the maximum number of edges to reach every other node
            def bfs(edges, x):
                # seen
                seen = set()

                # queue
                q = collections.deque([x])

                # max edges
                medges = -math.inf

                count = 0

                while q:

                    node = q.popleft()

                    # find edges
                    for e in edges:
                        if node == e[0] and e[1] not in q and e[1] not in seen:
                            q.append(e[1])
                            count += 1
                        elif node == e[1] and e[0] not in q and e[0] not in seen:
                            q.append(e[0])
                            count += 1

                    seen.add(node)


            bfs(edges, x)






        # reture the nodes that have the minimum of the maximum number
