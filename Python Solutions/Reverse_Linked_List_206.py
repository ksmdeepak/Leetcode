# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        prev = None
        curr = head
        nex = head.next
        
        while True:
            curr.next = prev
            prev = curr
            curr=nex
            if curr is None:
                break
            nex = nex.next
        return prev
