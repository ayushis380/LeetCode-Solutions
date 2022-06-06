class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> m = new HashMap<>();
        int start =0, resLen= 0;
        for(int end=0; end< fruits.length; end++){
            m.put(fruits[end], m.getOrDefault(fruits[end],0)+1);
            while(m.size() >2){
                m.put(fruits[start], m.getOrDefault(fruits[start],0)-1);
                if(m.get(fruits[start]) == 0)
                    m.remove(fruits[start]);
                start++;
            }
            resLen = Math.max(end-start+1, resLen);
        }
        return resLen;
    }
}
