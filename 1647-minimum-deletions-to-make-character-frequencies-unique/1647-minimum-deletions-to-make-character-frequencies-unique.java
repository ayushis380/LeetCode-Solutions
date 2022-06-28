class Solution {
    public int minDeletions(String s) {
        Map<Character, Integer> m = new HashMap<>();
        Set<Integer> st = new HashSet<>();
        for(int i=0; i< s.length(); i++){
            char ch = s.charAt(i);
            m.put(ch, m.getOrDefault(ch,0)+1);
        }
        int count =0;
        for(Map.Entry<Character, Integer> k: m.entrySet()){
            int val = k.getValue();
            while(st.contains(val)){
                // System.out.println(k.getKey() + " in while");
                count++;
                m.put(k.getKey(), k.getValue()-1);
                val = k.getValue();
            }
            if(!st.contains(val) && val!=0){
                st.add(val);
            }
        }
        return count;
    }
}