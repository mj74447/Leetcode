# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    global Mirror
    def Mirror(root1,root2)->bool:
        if root1 is None and root2 is None:
            return True
        if(root1 is not None and root2 is not None):
            if root1.val==root2.val:
                return(Mirror(root1.left,root2.right))and Mirror(root1.right,root2.left) 
            
        return False   
    def isSymmetric(self, root: TreeNode) -> bool:
        return Mirror(root,root)
