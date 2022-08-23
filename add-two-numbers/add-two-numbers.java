/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 
    [6,4,3], l2 = [5,6,4]
Output: [1,1,8]
Explanation: 346 + 465 = 811.
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode head = dummy;
        int carry =0;
        while(l1!= null || l2!= null || carry!=0){
            int val1 = (l1 ==null) ? 0: l1.val;
            int val2 = (l2 ==null) ? 0: l2.val;
            int sum = (val1+ val2+ carry);
            // System.out.println("before sum: "+ sum);
            carry = sum/10;
            // System.out.println("carry: "+carry);
             // System.out.println("after sum: "+ sum);
            head.next = new ListNode(sum%10);
            head = head.next;
            if(l1!=null)
                l1= l1.next;
            if(l2!=null)
                l2= l2.next;
        }
        return dummy.next;
            
    }
}