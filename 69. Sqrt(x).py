class Solution:
    def mySqrt(self, x: int) -> int:
        
        #Newton's iteration method
        root = x 
        
        while root**2 > x:
            
            root = (root + x//root) // 2
            
        return root