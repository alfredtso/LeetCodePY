import collections
import math
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        >>> sol = Solution()
        >>> n = 6
        >>> edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
        >>> sol.findMinHeightTrees(n, edges)
        [3, 4]
        >>> n = 1
        >>> edges = []
        >>> sol.findMinHeightTrees(n, edges)
        [0]
        >>> n = 2
        >>> edges = [[0,1]]
        >>> sol.findMinHeightTrees(n, edges)
        [0, 1]

        :param n:
        :param edges:
        :return:
        """

        # base case
        if n <= 2:
            return [i for i in range(n)]

        # construct the adjacent list from edges, undirected graph
        adj_list = [set() for i in range(n)]
        for i, j in edges:
            adj_list[i].add(j)
            adj_list[j].add(i)

        # create a queue and enqueue all the leaf node (which is node with only one neighbor)
        queue = collections.deque([])
        for i in range(n):
            if len(adj_list[i]) == 1:
                queue.append(i)

        # BFS until we are left with 2 nodes
        remaining_node = n
        while remaining_node > 2:
            remaining_node -= len(queue)
            new_queue = collections.deque([])
            # remove the leaf node and their associating edges
            while queue:
                leaf = queue.popleft()

                # Get the neighbor since 1. we need to remove the edge, 2. the only possible next leaves are neighbors
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)

                # check if neighbor becomes a leaf
                if len(adj_list[neighbor]) == 1:
                    new_queue.append(neighbor)

            queue = new_queue

        return list(queue)

if __name__ == '__main__':
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    n = 6
    sol = Solution()
    sol.findMinHeightTrees(n, edges)
    import doctest
    doctest.testmod()
