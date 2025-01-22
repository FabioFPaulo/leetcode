class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()

        while len(l) > 2:
            # remove first
            l = l[1::]
            # remove last
            l = l[0:len(l)-1]
            
        if len(l) == 2:
            return sum(l) / 2
        
        return l[0]

        
