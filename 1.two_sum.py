class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        
        for i, value in enumerate(nums):
            
            remaining = target - value
            
            if remaining in visited:
                return [i,visited[remaining]]
            
            visited[value] = i