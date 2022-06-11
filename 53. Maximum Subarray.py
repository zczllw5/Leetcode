class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxS = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0 :
                curSum = 0
            curSum += n
            maxS = max(maxS, curSum)
        return maxS    
        
#sliding window: incrementing right pointer while remove any prefix that have a negative value