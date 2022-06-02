class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I':1, 
            "V":5, 
            "X":10,
            "L":50,
            "C":100,
            "D":500, 
            "M":1000
        }
          
        res = 0
        
        for i in range(len(s) - 1):
            if map.get(s[i]) >= map.get(s[i + 1]):
                res += map.get(s[i])
            else:
                res -= map.get(s[i])

        return res + map.get(s[-1]) # trick is last one alway added 