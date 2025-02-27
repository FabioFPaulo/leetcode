class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        i = 0
        while i < len(words):
            word1 = words[i]
            word2 = words[i+1] if i + 1 < len(words) else words[0]

            c1 = word1[-1]
            c2 = word2[0]

            if c1 != c2:
                return False
            
            i+=1
        return True
