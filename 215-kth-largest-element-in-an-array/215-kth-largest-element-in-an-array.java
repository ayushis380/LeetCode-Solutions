class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> check = new PriorityQueue<>((a,b)-> a-b);
        for(int val: nums){
            check.add(val);
            if(check.size()> k)
                check.remove();
        }
        return check.remove();
    }
}