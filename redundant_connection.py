import array
import collections
from typing import List


class Solution:
    def findLeetCode(self, edges):
        """
        >>> sol = Solution()
        >>> edges = [[1,2],[1,3],[2,3]]
        >>> sol.findLeetCode(edges)
        [2, 3]
        >>> edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        >>> sol.findLeetCode(edges)
        [1, 4]
        >>> edges = [[1,2],[2,3],[1,3]]
        >>> sol.findLeetCode(edges)
        [1, 3]

        """
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)

                # base case
                if source == target:
                    return True

                # for loop or while loop
                return any(dfs(x, target) for x in graph[source])

        for u, v in edges:
            seen = set()

            # see if a path already exist in the graph we have built so far, if so return [u, v]
            # therefore it must be the later edge
            if u in graph and v in graph and dfs(u, v):
                return [u,v]
            graph[u].add(v)
            graph[v].add(u)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        >>> sol = Solution()
        >>> edges = [[1,2],[1,3],[2,3]]
        >>> sol.findRedundantConnection(edges)
        [2, 3]
        >>> edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        >>> sol.findRedundantConnection(edges)
        [1, 4]
        >>> edges = [[1,2],[2,3],[1,3]]
        >>> sol.findRedundantConnection(edges)
        [1, 3]

        """
        # TODO: dfs to detect cycle

        # initialize arrays
        # 0: undiscovered, 1: discovered, 2: processed
        parent = [0] * (len(edges) + 1)
        discovered_or_processed = [0] * (len(edges) + 1)
        adj_list = [[] for _ in range(len(edges) + 1)]
        finished = False
        result = []

        # start
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        def dfs(graph, s):
            nonlocal finished
            discovered_or_processed[s] = 1

            if finished:
                return

            for target in adj_list[s]:
                if discovered_or_processed[target] == 0:
                    parent[target] = s
                    process_edge(s, target)
                    dfs(graph, target)
                elif discovered_or_processed[target] != 2 and parent[s] != target:
                    process_edge(s, target)

                # early terminate
                if finished:
                    return

            # change node to processed
            discovered_or_processed[s] = 2

        def process_edge(x, y):
            nonlocal finished
            nonlocal result
            if parent[y] != x:
                if [x, y] in edges:
                    result = [x, y]
                else:
                    result = [y, x]

        dfs(edges, len(edges))
        return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
