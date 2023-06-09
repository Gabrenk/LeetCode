# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def recursive(root):
            if not root:
                return
            recursive(root.left)
            result.append(root.val)
            recursive(root.right)
        
        recursive(root)
        return(result)
