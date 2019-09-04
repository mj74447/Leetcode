# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = headA
        l2 = headB
        while(l1 != l2):
            l1 = headB if l1==None else l1.next
            l2 = headA if l2==None else l2.next
        return l1
