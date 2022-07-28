class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String str = paragraph.replaceAll("[^a-zA-Z0-9]"," ").toLowerCase();
        String[] arrWords = str.split("\\s+");
        
        Map<String, Integer> m = new HashMap<>();
        for(int i=0; i< arrWords.length; i++){
            String val = arrWords[i];                
            m.put(val, m.getOrDefault(val,0)+1);
        }
        for(int i=0; i< banned.length; i++){
            String val = banned[i];                
            if(m.containsKey(val))
                m.remove(val);
        }
        // int maxCount =0;
        // String res = "";
        // for(Map.Entry<String, Integer> e: m.entrySet()){
        //     System.out.println("Key- " + e.getKey() + ", Value- " + e.getValue());
        //     if(maxCount < e.getValue()){
        //         maxCount = e.getValue();
        //         res = e.getKey();
        //     }
        // }
        return Collections.max(m.entrySet(), Map.Entry.comparingByValue()).getKey();
        }
    }
