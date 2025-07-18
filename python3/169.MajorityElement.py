class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key_value = defaultdict(int)
        res, maxCount = 0,0
        for n in nums:
            key_value[n] +=1

            res = n if key_value[n] > maxCount else res
            maxCount = max(key_value[n], maxCount)

        return res
