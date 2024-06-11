# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        
        lengthA = 0
        lengthB = 0
        while curA:
            lengthA += 1
            curA = curA.next
        while curB:
            lengthB += 1
            curB = curB.next

        skip = lengthA - lengthB
        curA = headA
        curB = headB
        if skip > 0:
            for i in range(skip):
                curA = curA.next
        elif skip < 0:
            for i in range(-skip):
                curB = curB.next
                
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None