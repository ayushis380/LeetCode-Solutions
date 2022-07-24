class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List> m = new HashMap<>();
        List<List<String>> res = new ArrayList<>();
        for(int i=0; i< strs.length; i++){
            char[] ch = strs[i].toCharArray();
            Arrays.sort(ch);
            String s = String.valueOf(ch);
            if(!m.containsKey(s)){
                m.put(s, new ArrayList());
            }
            m.get(s).add(strs[i]);
        }
        return new ArrayList(m.values());
    }
}