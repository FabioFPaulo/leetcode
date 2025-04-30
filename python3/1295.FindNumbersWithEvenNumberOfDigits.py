class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        output = 0

        for number in nums:
            n = len(f"{number}")
            if n % 2 == 0:
                output +=1
        return output
