class Solution:
    def myAtoi(self, s: str) -> int:
        number = 0
        #ignore leading spaces
        s =s.lstrip(' ')
            
        if s[0] == '+':
            s = s[1:]
            print("positive removed")
        
        if s[0].isdigit() or s[0] == '-':
            number = re.sub('[^0-9-.]','', s)
            
            if float(number) > 2147483647: return 2147483647
            if float(number) < -2147483648: return -2147483648
            # if isinstance(1.0): return int(number)
            # print(number)
        else:
            return 0
        
        return int(float(number))