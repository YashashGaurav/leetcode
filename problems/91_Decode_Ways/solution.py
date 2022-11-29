'''
    91. Decode Ways
'''

class Solution:

    # neetcoded
    # Accepted	62 ms	13.8 MB
    def numDecodings(self, s: str) -> int:
        
        # makes sure if s is of any length,
        # which it will be as given in the contraint,
        # There is atleast one possible decoding
        store = {len(s) : 1} 
        
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                store[i] = 0
            else:
                store[i] = store[i+1]
                
            if (i + 1 < len(s)) and ((s[i] == '1') or 
                                     (s[i] == '2' and s[i+1] in '0123456')):
                store[i] += store[i+2]
                                     
        return store[0] 