class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String newString = paragraph.replaceAll("[^a-zA-Z0-9]"," ").toLowerCase();
        String[] splitarr = newString.split("\\s+");
        Map<String,Integer> m = new HashMap<String,Integer>();
        Set<String> setBanned = new HashSet<>();
        for(String str: banned)
            setBanned.add(str);
        for(int i=0; i<splitarr.length; i++){
            if(!setBanned.contains(splitarr[i]))
                m.put(splitarr[i], m.getOrDefault(splitarr[i],0)+1);
        }
       // Collections.max(mapName.entrySet(), Map.Entry.comparingByValue()).getKey();
        
        return Collections.max(m.entrySet(), Map.Entry.comparingByValue()).getKey();
        
    }
}