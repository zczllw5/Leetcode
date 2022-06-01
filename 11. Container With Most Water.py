class Solution:
    def maxArea(self, height: List[int]) -> int:
        area  = 0 
        
        l, r = 0, len(height) - 1
        
        while l < r:
            temp = min(height[l], height[r]) * (r - l)

            if temp > area: area = temp
            
            if height[l] >=  height[r]: 
                r -= 1 
            else:
                l += 1
            
        return area