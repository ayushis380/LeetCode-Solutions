class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> sumFreq = new HashMap<>(); // store the number of times a particular sum is found. We use this approach as numbers are both +ve and -ve
        // prefix sum = (x-k) + k  - finding only k is difficult 
        // (x-k) - finding this is easier as its just storing (x-k) sum and its freq
        // number of times we find (x-k) is equal to number of times we will find k
        sumFreq.put(0,1); // when first element itself is equal to k
        int prefixsum =0, count =0;
        for(int i=0; i< nums.length; i++){
            prefixsum+= nums[i];
            if(sumFreq.containsKey(prefixsum - k))
                count+= sumFreq.get(prefixsum - k);
            sumFreq.put(prefixsum, sumFreq.getOrDefault(prefixsum,0)+1);
        }
        return count;
    }
}