# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        cursor = head
        while cursor != None:
            count += 1
            cursor = cursor.next
            
        middle_count = count // 2
        for _ in range(middle_count):
            head = head.next
        return head