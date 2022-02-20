/* 
Merge Nodes in Between Zeros
[Medium]
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
 
class Solution {
    public ListNode mergeNodes(ListNode head) {
        ListNode curr = new ListNode();
        ListNode res = curr;
        int sum=0;
        while(head.next!=null){
            head = head.next;
            if(head.val!=0){
                sum+= head.val;
            }
            else{
                ListNode temp = new ListNode(sum);
                curr.next = temp;
                curr = temp;
                sum=0;
            } 
        }
        return res.next;
    }
}
