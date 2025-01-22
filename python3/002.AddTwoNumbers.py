# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mlist = ListNode(0)
        head = mlist

        expoent = 0
        while l1 or l2 or expoent:
            x = 0
            if l1:
                x = l1.val
                l1 = l1.next

            y = 0
            if (l2):
                y = l2.val
                l2 = l2.next

            number = x + y + expoent
            expoent = 0
            while number >= 10:
                number -= 10
                expoent +=1
            
            newNode = ListNode(number)
            head.next = newNode
            head = newNode
        
        return mlist.next
    
