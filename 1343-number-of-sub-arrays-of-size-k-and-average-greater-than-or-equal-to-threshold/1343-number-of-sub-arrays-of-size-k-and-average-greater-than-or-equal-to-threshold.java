class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int count =0;
        int sum=0, start =0;
        for(int i=0; i< arr.length; i++){
            sum += arr[i];
            if(i-k>= -1){
                // System.out.println("Inside if\n");
                // System.out.println(sum);
                if(sum/k >= threshold)
                    count++;
                sum -= arr[start];
                start++;
            }
        }
        return count;
    }
}