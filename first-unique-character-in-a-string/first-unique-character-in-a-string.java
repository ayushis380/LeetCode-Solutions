class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> mapStore = new HashMap<>();
        for(int i=0; i< s.length(); i++){
            char ch = s.charAt(i);
            mapStore.put(ch, mapStore.getOrDefault(ch,0)+1);
        }
        for(int i=0; i< s.length(); i++){
            int val = mapStore.get(s.charAt(i));
            if(val == 1)
                return i;
        }
        return -1;
    }
}