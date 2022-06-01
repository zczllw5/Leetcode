class Solution:
    def reverse(self, x: int) -> int:
        
        reversed = 0
        
        if x > 0:
            reversed = self.helper(x, reversed)
            return reversed
        else:
            x = -x
            reversed = self.helper(x, reversed)
            reversed = - reversed
            return reversed
        
    def helper(self, x: int, reversed: int):
        
        while x != 0:

            digit = x % 10   # get the digit to be reverse
            x = x // 10      # remove the digit
            
            if reversed * 10 + digit < 2 ** 31 - 1:
                reversed = reversed * 10 + digit  # build the reversed
            else:
                reversed = 0  
                
        return reversed
            
            
    