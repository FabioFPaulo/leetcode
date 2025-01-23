class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0

        idx = 0
        while idx < len(s):
            if idx < len(s) - 1:
                if d[s[idx]] < d[s[idx+1]]:
                    count = d[s[idx+1]] - d[s[idx]]
                    res += count
                    idx +=2
                    continue
                else:
                    res += d[s[idx]]
            else:
                res += d[s[idx]]
            idx +=1


        return res
        
