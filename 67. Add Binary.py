#method 1
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a, b = int(a,2), int(b,2)
        sum = a + b
        return "{0:b}".format(sum)

#method 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
            
        carry = 0
        res = ''
        
        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
                
            res += str(carry % 2)
            
            carry //= 2 
        
        return res[::-1]