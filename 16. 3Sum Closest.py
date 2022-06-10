class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        closest = nums[0] + nums[1] + nums[2]
        
        nums.sort()
        
        for i in range(len(nums) - 2):
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                
                sum = nums[i] + nums[l] + nums[r]
                dif = sum - target
                
                if abs(dif) < abs(closest - target):
                    closest = sum
                
                if dif >= 0:
                    r -= 1
                else:
                    l += 1
                    
        return closest