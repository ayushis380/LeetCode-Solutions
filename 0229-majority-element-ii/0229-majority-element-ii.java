class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<>();
        int ct1 = 0, ct2 = 0; // atmost 2 elements can be there
        int el1 = 0, el2 = 0; // Moores algo
        for(int i=0; i< nums.length; i++){
            if(ct1 == 0 && el2 != nums[i]){  // if we dont check el2 != nums[i]
            // then a case can occur that el1 and el2 have same value
                ct1++;
                el1 = nums[i];
            } 
            else if(ct2 == 0 && el1 != nums[i]){// if we dont check el1 != nums[i]
            // then a case can occur that el1 and el2 have same value
                ct2++;
                el2 = nums[i];
            } 
            else if(nums[i] == el1)
                ct1++;
            else if(nums[i] == el2)
                ct2++;
            else{
                ct1--; // other element canceling el1 count
                ct2--; // some other element canceled el2 count
            }
        }
        System.out.println(el1 + " " + el2);
        ct1 =0; ct2 =0; 
        for(int i=0; i< nums.length; i++){
            if(nums[i] == el1)
                ct1++;
            else if(nums[i] == el2)
                ct2++;
        }
        int minreq = (nums.length/3) +1; // this is the required count 
        if(ct1 >= minreq)
            res.add(el1);
        if(ct2 >= minreq)
            res.add(el2);
        return res;
    }
}