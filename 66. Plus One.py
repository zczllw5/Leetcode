class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        
        one, i = 1, 0 
        
        while one:
            if i < len(digits): #inbound 
                if digits[i] == 9:
                    #one = 1
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0     #no carry
            else:               #outbound
                digits.append(1)
                one = 0
                
            i += 1
            
        return digits[::-1]