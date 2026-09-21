# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            currentDiameter = leftHeight + rightHeight
            self.diameter = max(self.diameter, currentDiameter)

            currentHeight = 1 + max(leftHeight, rightHeight)
            return currentHeight

        dfs(root)
        return self.diameter