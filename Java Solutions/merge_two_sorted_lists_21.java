/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1==null)
            return l2;
        else if (l2==null)
            return l1;
        ListNode a,b;
        if (l1.val<l2.val){
            a=l1;
            b=l2;
        }
        else{
            a=l2;
            b=l1;
        }
        ListNode head = a;
        while(a!=null && b!=null){
            
            if (a.val>b.val){
                ListNode temp =a;
                a=b;
                b=temp;
            } 
            if(a.next==null){
                a.next=b;
                break;
            }
                
            if(a.next.val > b.val){
                ListNode temp=a.next;
                a.next = b;
                a = temp;
            }
            else{
                a= a.next;
            }
        }
        return head;
        
    }
}