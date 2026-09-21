# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.indices = {val: idx for idx, val in enumerate(inorder)}
        self.preIdx = 0

        def dfs(l, r):
            if l > r:
                return None

            # get current root from preorder
            rootVal = preorder[self.preIdx]
            root = TreeNode(rootVal)
            self.preIdx += 1

            # find root in inorder
            mid = self.indices[rootVal]

            # left of mid -> left subtree
            root.left = dfs(l, mid - 1)

            # right of mid -> right subtree
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)
