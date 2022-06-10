class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            #print([i,nums[i]])
            if i > 0 and nums[i] == nums[i - 1]: #same value as before
                continue
                
            l, r = i + 1, len(nums) - 1 
            
            while l < r:
                
                threesum = nums[i] + nums[l] + nums[r]
                
                if threesum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    l += 1                                      #update the pointer  
                    while nums[l] == nums[l - 1] and l < r:     #keep shifting until nums[l] is a dif value
                        l += 1
                        
                elif threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
            
        return res

