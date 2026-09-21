# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = root.val

        def dfs(node):
            if not node:
                return

            # visit smaller values
            dfs(node.left)
            
            # early exit
            if self.count == k:
                return

            # visit current node
            self.count += 1
            if self.count == k:
                self.res = node.val
                return

            # visit larger values
            dfs(node.right)
        
        dfs(root)
        return self.res
