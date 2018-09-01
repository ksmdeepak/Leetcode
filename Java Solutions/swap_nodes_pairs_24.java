/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swap(ListNode p){
        if(p==null)
            return null;
        ListNode temp;
        if(p.next==null)
            return p;
        else{
            temp =p.next;
            p.next = p.next.next;
            temp.next =p;
        }
        return temp;
    }
    public ListNode swapPairs(ListNode head) {
        if(head==null)
            return head;
        ListNode temp=head;
        head = swap(head);
        ListNode tail = head.next;
        while(tail!=null && tail.next!=null ){
            tail.next = swap(tail.next);
            if(tail.next.next!=null)
                tail= tail.next.next;
            else
                tail=tail.next;
        }
        return head;
    }
}