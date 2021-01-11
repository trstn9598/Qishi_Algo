# recursion with one shared variable

class Solution:
    def __init__(self):
        self.res = -float('inf')
        
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            l, r = helper(root.left), helper(root.right)
            l, r = max(0, l), max(0, r)
            self.res = max(self.res, l+r+root.val) 
            
            return max(l, r) + root.val
        helper(root)
        return self.res
