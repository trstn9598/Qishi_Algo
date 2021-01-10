# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            res = l1
            p = l1.next
            res.next = self.mergeTwoLists(p,l2)
            return res
        else:
            res = l2
            p = l2.next
            res.next = self.mergeTwoLists(l1,p)
            return res
            
            
                
            
   
