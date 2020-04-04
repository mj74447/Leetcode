'''Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24. '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
          
        def leaf_sum(self,root): 
            
            if root is None:
                            return 0
            
            if root.left and not root.left.left and not root.left.right: #Condition to check if there's a left leaf
                self.sum += root.left.val
                
            leaf_sum(self,root.left)
            leaf_sum(self,root.right)
            
            
        leaf_sum(self,root)
        return self.sum
