class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a,b)-> a[1]-b[1]);
        Queue<Integer> hp = new PriorityQueue<>((a,b)-> b-a);
        int time=0;
        for(int[] arr: courses){
            if(time+arr[0] <= arr[1]){
                time+= arr[0];
                hp.offer(arr[0]);
            }else if(!hp.isEmpty() && hp.peek() > arr[0]){
                time+= arr[0] - hp.poll();
                hp.offer(arr[0]);
            }
        }
        return hp.size();
    }
}