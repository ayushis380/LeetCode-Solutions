class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] nums1c = new int[m];
        for(int i=0; i<m; i++){
           nums1c[i] = nums1[i];
       }
       int p1= 0, p2 = 0; // always check that p1 is not greater than m and if p2 is greater than n it means now p1 values are remaining to be updated
        for(int p=0; p< m+n; p++){
            if(p2>=n ||( p1<m && nums1c[p1] < nums2[p2]))
                nums1[p] = nums1c[p1++];
            else
                nums1[p] = nums2[p2++];
        }
    }
}