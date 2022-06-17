class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left root right
        
        res = []
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        inorder(root)
        
        return res