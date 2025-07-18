import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        count = -1
        res = 0

        c_head = head
        while (c_head != None):
            count +=1
            c_head = c_head.next

        x_head = head
        while x_head != None:
            res += x_head.val * math.pow(2, count)
            count -=1
            x_head = x_head.next
        
        return int(res)
        


