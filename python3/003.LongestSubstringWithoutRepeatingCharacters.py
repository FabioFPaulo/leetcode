class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        

        for i in range(len(s)):
            new_string =  s[i]
            

            j = i+1
            while j < len(s):
                if s[j] in new_string:
                    break
                else:
                    new_string = new_string + s[j]
                    j+=1

            if len(new_string) > len(string):
                string = new_string

            new_string = ""

        print(string)
        return len(string)

