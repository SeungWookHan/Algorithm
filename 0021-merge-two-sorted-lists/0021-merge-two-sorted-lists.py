# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        head = sortedList = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                sortedList.next = list1
                list1 = list1.next
            else:
                sortedList.next = list2
                list2 = list2.next
            
            sortedList = sortedList.next
        sortedList.next = list1 or list2 
        return head.next