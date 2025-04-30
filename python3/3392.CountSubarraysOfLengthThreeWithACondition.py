class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l = len(nums)
        output = 0

        for x in range(0, l-2):
            n1 = nums[x]
            n2 = nums[x+1]
            n3 = nums[x+2]
            
            if n1+n3 == n2/2:
                output+=1


        return output
