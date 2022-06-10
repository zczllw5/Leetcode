class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in dict:                                   #1
                stack.append(i)
            elif len(stack) == 0 or dict[stack.pop()] != i: #2
                    return False
        return len(stack) == 0                              #3

# 1. if it's a left parentheses
# 2. if it's right parenthese, compare to the previous one. If doesn't match return false
# 3. finaly check the stack if it's empty after all input processed