class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b) ->a[0]-b[0]);
        LinkedList<int[]> res = new LinkedList<>();
        for(int[] arr: intervals){
            if(res.isEmpty() || res.getLast()[1] < arr[0])
                res.add(arr);
            else
                res.getLast()[1] = Math.max(res.getLast()[1], arr[1]);
        }
    return res.toArray(new int[res.size()][]);
    }
}