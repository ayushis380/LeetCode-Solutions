class Solution {
    public int findPeakElement(int[] nums) {
//         int start =0, end =nums.length-1;
//         while(start<=end){
//             int mid = start + (end-start)/2 ;
            
//             }
        for(int i=0; i<= nums.length-1; i++){
            int count =0;
            if(i-1 < 0 || nums[i-1] < nums[i])
                count++;
            if(i+1>= nums.length || nums[i+1] < nums[i])
                count++;
            if(count ==2)
                return i;
        }
        return 0;
        
    }
}