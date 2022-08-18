/**
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
    public ListNode reverseList(ListNode head) {
        ListNode new_head = null;
        while(head != null){
            ListNode new_node = head.next;
            head.next = new_head;
            new_head = head;
            head = new_node;
        }
        return new_head;
    }
}