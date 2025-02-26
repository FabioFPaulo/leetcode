class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        len_strs = len(strs)

        i = 0
        _chr = None
        helper = 0
        pointer = 0
        while i < len_strs:
            len_str = len(strs[i])
            if _chr == None and pointer < len_str:
                _chr = strs[i][pointer]
                helper +=1
                
            elif  pointer < len_str and _chr == strs[i][pointer]:
                helper +=1

            if helper == len_strs:
                helper = 0
                i = 0
                pointer+=1
                prefix += _chr
                _chr = None
            else:
                i+=1
        return prefix




        
