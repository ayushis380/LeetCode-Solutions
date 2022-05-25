class Solution {
    private HashMap<String, Integer> wC = new HashMap<>();
    private int eachWordLen, subLen, wordsLen;
    public List<Integer> findSubstring(String s, String[] words) {
        int sLen = s.length();
        wordsLen = words.length;
        eachWordLen = words[0].length();
        subLen = wordsLen * eachWordLen;
        List<Integer> res = new ArrayList<>();
        for(String str: words){
            wC.put(str, wC.getOrDefault(str,0)+1);
        }
        for(int i=0; i< sLen- subLen+1; i++){
            if(check(i,s))
                res.add(i);
        }
        return res;
        
    }
    public boolean check(int i, String s){
        HashMap<String, Integer> rem = new HashMap<>(wC);
        int wordsUsed =0;
        for(int j=i; j< i+ subLen; j+=eachWordLen){
            String sub = s.substring(j, j+eachWordLen);
            if(rem.getOrDefault(sub,0) != 0){
                rem.put(sub, rem.get(sub)-1);
                wordsUsed++;
            }
            else
                break;
        }
        return wordsUsed == wordsLen;
    }
    
}