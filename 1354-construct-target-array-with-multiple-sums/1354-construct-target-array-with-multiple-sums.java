class Solution {
    public boolean isPossible(int[] target) {
        
        if (target.length == 1) {
            return target[0] == 1;
        }
        
        int totalSum = Arrays.stream(target).sum();
        
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        for (int num : target) {
            pq.add(num);
        }
        
        while (pq.element() > 1) {
            int largest = pq.remove();
            int rest = totalSum - largest;
            
            if (rest == 1) {
                return true;
            }
            int x = largest % rest;

            if (x == 0 || x == largest) {
                return false;
            }
            pq.add(x);
            totalSum = totalSum - largest + x;
        }
        
        return true; 
    }
}