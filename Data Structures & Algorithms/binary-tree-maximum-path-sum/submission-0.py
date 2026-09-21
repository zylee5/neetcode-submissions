# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # best single downward branch from left child
            leftDownSum = max(0, dfs(node.left))

            # best single downward branch from right child
            rightDownSum = max(0, dfs(node.right))

            # best path with current node as turning point
            throughNodeSum = node.val + leftDownSum + rightDownSum
            self.res = max(self.res, throughNodeSum)

            # parent can extend through this node using only one side of the path
            downSumFromNode = node.val + max(leftDownSum, rightDownSum)
            return downSumFromNode
        
        dfs(root)
        return self.res
