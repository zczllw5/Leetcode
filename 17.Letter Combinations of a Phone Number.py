class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            "2":"abc",
            "3":"def", 
            "4":"ghi", 
            "5":"jkl", 
            "6":"mno", 
            "7":"pqrs", 
            "8":"tuv", 
            "9":"wxyz"
        }
        
        res = []
        
        if not digits: return res
        
        if len(digits) == 1:
            #return list(hashmap[digits[0]])
            return [c for c in hashmap[digits[0]]]
        
        pre = self.letterCombinations(digits[:-1])
        additional = hashmap[digits[-1]]
        return [s + c for s in pre for c in additional]