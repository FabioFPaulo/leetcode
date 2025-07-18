class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        for num in nums:
            count += num

            remain = count % k

            if remain in prefix_count:
                res += prefix_count[remain]
            prefix_count[remain] +=1

        return res
