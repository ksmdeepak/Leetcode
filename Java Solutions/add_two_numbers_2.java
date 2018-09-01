/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
    ListNode output = new ListNode(0);
    ListNode temp = output;
    ListNode p=l1;
    ListNode q=l2;  
    int carry=0;
    while(p!=null || q!=null){
         int pv = p!=null ? p.val : 0;
         int qv = q!=null ? q.val : 0;
         int value = (pv+qv+carry);
         temp.next = new ListNode(value%10);  
         carry = value/10;
        if(p!=null)
             p=p.next;
        if(q!=null)
             q=q.next;
        temp=temp.next;

    }
    if(carry==0)
        temp.next=null;
    else
        temp.next = new ListNode(carry);  
    return output.next;
}
}