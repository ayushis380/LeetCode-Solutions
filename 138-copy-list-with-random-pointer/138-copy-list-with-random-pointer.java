/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    HashMap<Node, Node> nodeMap = new HashMap<Node, Node>();
    public Node copyRandomList(Node head) {
        if(head == null)
            return null;
        if(nodeMap.containsKey(head))
            return nodeMap.get(head);
        Node n = new Node(head.val, null, null);
        nodeMap.put(head, n);
        n.next = copyRandomList(head.next);
        n.random = copyRandomList(head.random);
        return n;
    }
}