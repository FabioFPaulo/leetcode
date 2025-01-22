class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index1 in range(len(nums)):
            for index2 in range(len(nums) - 1):
                if nums[index1] + nums[index2] == target and index1 != index2:
                    return [index1, index2]
        
