# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def BST(root):
            #leaf
            if not root.left and not root.right:
                return True, root.val, root.val
            elif not root.left:
                RBool, RMax, RMin = BST(root.right)
                return (RBool and root.val < RMin), max(root.val,RMax), min(root.val, RMin)
            elif not root.right:
                LBool, LMax, LMin = BST(root.left)
                return (LBool and root.val > LMax), max(root.val, LMax), min(root.val, LMin)
            else:
                RBool, RMax, RMin = BST(root.right)
                LBool, LMax, LMin = BST(root.left)
                return (LBool and RBool and LMax < root.val < RMin), RMax, LMin
        Bool, Max, Min = BST(root)
        return Bool
            
                
               
