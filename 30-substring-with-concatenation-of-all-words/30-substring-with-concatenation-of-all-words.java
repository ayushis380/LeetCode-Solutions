class Solution {
    private HashMap<String, Integer> wC = new HashMap<>();
    private int sLen, wordsLen, eachWordLen, subStrSize;
    public List<Integer> findSubstring(String s, String[] words) {
        sLen = s.length();
        wordsLen = words.length;
        eachWordLen = words[0].length();
        subStrSize = wordsLen * eachWordLen;
        for(String str: words){
            wC.put(str, wC.getOrDefault(str,0)+1);
        }
        List<Integer> res = new ArrayList<>();
        for(int i=0; i< eachWordLen; i++){
            check(i,s, res);
        }
        return res;
    }
    private void check(int left, String s, List<Integer> res){
        HashMap<String, Integer> wF = new HashMap<String, Integer>();
        int wordsUsed =0; 
        boolean excessWord= false;
        for(int right= left; right<= sLen- eachWordLen; right+= eachWordLen){
            String sub = s.substring(right, right+eachWordLen);
            if(!wC.containsKey(sub)){
                wF.clear();
                wordsUsed =0;
                excessWord = false;
                left= right + eachWordLen;
            } else{
                while(right-left == subStrSize || excessWord){
                    String leftmostWord = s.substring(left, left+eachWordLen);
                    // System.out.println(leftmostWord);
                    left+= eachWordLen;
                    wF.put(leftmostWord, wF.get(leftmostWord)-1);
                    if(wF.get(leftmostWord) >= wC.get(leftmostWord)){
                        excessWord = false;
                    }else{
                        wordsUsed--;
                    }
                }
                wF.put(sub, wF.getOrDefault(sub,0)+1);
                if(wF.get(sub) > wC.get(sub)){
                    excessWord = true;
                }
                else 
                    wordsUsed++;
                if(wordsUsed == wordsLen && !excessWord)
                    res.add(left);
            }
        }
    }
}