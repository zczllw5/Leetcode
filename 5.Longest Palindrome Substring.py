class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        
        for i in range(len(s)):  #loop throught the mid point and expand the palindrome from there
            
            #odd
            temp = self.helper(s, i, i)
            if len(temp) > len(res):
                res = temp
        
            #even
            temp = self.helper(s, i, i + 1)
            if len(temp) > len(res):
                res = temp
        
        return res
    
    #helper fucntion
    def helper(self, s, l , r) ->str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1;
        return s[l+1:r]