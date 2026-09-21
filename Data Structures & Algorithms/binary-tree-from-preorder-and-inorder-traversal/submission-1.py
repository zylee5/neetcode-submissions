# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIdx = 0
        self.inIdx = 0

        def dfs(limit):
            if self.preIdx >= len(preorder):
                return None
            if inorder[self.inIdx] == limit:
                self.inIdx += 1
                return None
            
            # preorder gives the next root
            rootVal = preorder[self.preIdx]
            root = TreeNode(rootVal)
            self.preIdx += 1

            # left subtree ends when inorder reaches the current root
            root.left = dfs(rootVal)

            # right subtree keeps the parent's boundary
            root.right = dfs(limit)
            return root
        
        return dfs(float('inf'))