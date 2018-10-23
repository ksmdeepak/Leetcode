# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        else:
            curr = head
            nxt = head.next
            ans = ListNode(0)
            temp = ans
            if curr and not nxt:
                    temp.next = curr
            while curr and nxt:
                if curr.val!=nxt.val:
                    temp.next = curr
                    curr = curr.next
                    nxt = nxt.next
                    temp = temp.next
                    temp.next = None
                    
                else:
                    while curr and curr.val==nxt.val:
                        curr = curr.next
                    if curr:
                        nxt = curr.next
                if curr and not nxt:
                    temp.next = curr
            return ans.next
