# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        mid = len(li) // 2
        if len(li) % 2 == 0:
            return li[:mid] == li[-1:mid-1:-1]
        else:
            return li[:mid] == li[-1:mid:-1]