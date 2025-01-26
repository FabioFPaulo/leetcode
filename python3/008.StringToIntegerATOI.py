class Solution:
    def myAtoi(self, s: str) -> int:
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        res = ""
        _range = [pow(-2, 31), pow(2, 31) -1]

        # Whitespace: Ignore any leading whitespace (" ")
        idx = 0
        while idx < len(s):
            if s[0] == " ":
                s = s.replace(" ", "", 1)
            idx+=1
        print(s)
        

        # Signedness: Determine the sign by checking if 
        # the next character is '-' or '+', assuming positivity if neither present.
        sign = "+0" 
        if len(s) > 0:
            if s[0] == "-":
                sign = "-0"
                s = s[1::]
            elif s[0] == "+":
                s = s[1::]

        res += sign
        

        #Conversion: Read the integer by skipping leading zeros 
        #until a non-digit character is encountered or the end of the string is reached. 
        #If no digits were read, then the result is 0
        idx = 0
        while (idx < len(s)) and (s[idx] in digits):
            res += s[idx]
            idx+=1
        

        # Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
        # then round the integer to remain in the range. Specifically, integers less than -231 
        # should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
        res = int(res)
        if res < _range[0]:
            res = _range[0]
        elif res > _range[1]:
            res = _range[1]

        
        return res





        
