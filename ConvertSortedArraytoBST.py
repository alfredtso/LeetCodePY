# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> None:

        def helper(left, right):

            # base case
            if left > right:
                return None

            # choose root node
            root_index = (left+right) // 2

            root = TreeNode(nums[root_index])
            root.left = helper(left, root_index-1)
            root.right = helper(root_index+1, right)

            return root

        return helper(0, len(nums)-1)

    def test(self):
        assert self.sortedArrayToBST([-10, -3, 0, 5, 9]) == [0, -3, 9, -10, None, 5] or [0, -10,5,None,-3,None,9]
        assert self.sortedArrayToBST([1,3]) == [1,3] or [3,1]


if __name__ == '__main__':
    my = Solution()
