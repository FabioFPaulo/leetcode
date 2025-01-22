class Solution:

    def isPal(self, s, i , j):
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True
    
    def longestPalindrome(self, s: str) -> str:
        pal = s[0]

        

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] and len(s[i:j+1]) > len(pal) and self.isPal(s, i, j):
                    pal = s[i:j+1]
        return pal
                    


            
        
