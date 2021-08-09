"""
>>> two = TreeNode(2)
>>> four = TreeNode(4)
>>> three = TreeNode(3, four, two)
>>> root = TreeNode(3, three)
>>> sol = Solution()
>>> sol.goodNodes(root)
3
"""
# Definition for a binary tree node.
import math
from collections import namedtuple

# Trying out namedtuple to encapsulate the value of so far into the Node
Node = namedtuple('Node', ['node', 'sofar'])

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs_helper(Node(root, -math.inf))

    def dfs_helper(self, n: Node) -> int:

        sofar = max(n.node.val, n.sofar)
        count = 0

        # increment count for this node
        if n.node.val >= n.sofar:
            count += 1

        # dfs
        if n.node.left:
            count += self.dfs_helper(Node(n.node.left, sofar))
        if n.node.right:
            count += self.dfs_helper(Node(n.node.right, sofar))

        return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
