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
    public ListNode mergeKLists(ListNode[] lists) {
       ListNode dummy = new ListNode(0);
        ListNode head = dummy;
        PriorityQueue<Integer> comp = new PriorityQueue<>((a,b)-> a-b);
        for(ListNode l: lists){
            while(l!=null){
            comp.offer(l.val);
            l= l.next;
            }
        }
        while(!comp.isEmpty()){
            head.next = new ListNode(comp.poll());
            head = head.next;
        }
        return dummy.next;
    }
}