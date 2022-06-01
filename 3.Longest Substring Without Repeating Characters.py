class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maxLen = 0
        
        for i, c in enumerate(s):
            
            if c not in substring:
                substring += str(c)
                maxLen = max(len(substring), maxLen)
            else:                
                #continue without repeating characters by start from current character
                
                #start from the second character of the 1st occurance of the repeating character
                #remove the 1st occurance of the repeating character
                
                substring += str(c)
                
                index = substring.find(c)
                substring = substring[index+1:]

        return maxLen