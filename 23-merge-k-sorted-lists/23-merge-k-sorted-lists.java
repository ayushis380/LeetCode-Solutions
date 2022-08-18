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
        List<Integer> arr = new ArrayList<>();
        for(ListNode l: lists){
            while(l!=null){
                arr.add(l.val);
                l= l.next;
            }
        }
        Collections.sort(arr);
        ListNode dummy = new ListNode(0);
        ListNode head = dummy;
        for(Integer i: arr){
            head.next = new ListNode(i);
            head = head.next;
        }
        head.next = null;
        return dummy.next;
    }
}