class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        
        sho = min(strs, key=len)
        
        for i in range(len(sho)):
            
            c = sho[i]
            
            for s in strs:
                if c == s[i]:
                    continue
                else:
                    return lcp
            lcp += c
        
        return lcp