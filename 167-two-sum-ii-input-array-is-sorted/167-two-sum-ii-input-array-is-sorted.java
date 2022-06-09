class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] res = new int[2];
        Map<Integer, Integer> m = new HashMap<>();
        for(int i=0; i<numbers.length; i++){
            int comp = target - numbers[i];
            if(m.containsKey(comp)){
                return new int[]{m.get(comp), i+1};
            }
            m.put(numbers[i], i+1);
        }
        return new int[] {-1,-1};
    }
}