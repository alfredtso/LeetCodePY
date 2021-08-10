from typing import List
from google.cloud import bigquery

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        >>> sol = Solution()
        >>> numCourses = 2
        >>> prerequisites = [[1,0]]
        >>> sol.canFinish(numCourses, prerequisites)
        True
        >>> numCourses = 2
        >>> prerequisites = [[1,0],[0,1]]
        >>> sol.canFinish(numCourses, prerequisites)
        False

        """
        # return False if cycle detected
        # produce adjacency list first ?
        adj_list = [set() for i in range(numCourses)]
        for i, j in prerequisites:
            # the prerequisite of j is i
            adj_list[j].add(i)

        # initialization
        # state: 0 undiscoved, 1 discovered, 2 processed
        state = [0] * numCourses
        parent = [-1] * numCourses
        entrytime = [-1] * numCourses
        exittime = [-1] * numCourses
        time = 0
        finished = False

        def process_edges(u, v):
            # classification of edges, we should just care about back edges
            # backedge: if v is discovered but not processed, edge (u,v) will be BACK
            nonlocal finished
            if state[v] == 1:
                finished = True

        def dfs(ls, u):
            nonlocal time
            nonlocal finished

            if finished:
                return

            # update the state
            time += 1
            state[u] = 1
            entrytime[u] = time

            # loop adjacent edges of u
            for e in ls[u]:
                # case: undiscovered, set parent, process edges and dfs
                if state[e] == 0:
                    parent[e] = u
                    # process_edges(u, second_vertex)
                    dfs(ls, e)
                # case: discovered, process edges
                elif state[e] == 1:
                    finished = True

                # terminate
                if finished:
                    return

            # visited all adj vertices
            state[u] = 2

            # update leave vertex time
            time += 1
            exittime[u] = time

        for i in range(numCourses):
            if state[i] == 0 and not finished:
                dfs(adj_list, i)

        return not finished

if __name__ == '__main__':
    import doctest
    doctest.testmod()

