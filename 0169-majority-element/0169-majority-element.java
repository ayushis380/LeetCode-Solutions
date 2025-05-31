class Solution {
    public int majorityElement(int[] nums) {
        // Moore's voting algo
        int count = 0, el =0;
        for(int i=0; i< nums.length; i++){
            if(count == 0){ // at this point in array it means 
            // the element el's count is countered negative by other elements which are not equal to el
            // this means that el's count will not be > n/2 as now its n/2; n being length till that point
                count = 1;
                el = nums[i];
            } else if(nums[i] == el)
                count++;
            else
                count--;
        }
        return el; // if majority element exists then el will be majority 
        // if a majority element doesnt exist then check count(el) > n/2 - if true then return el otherwise -1 
    }
}