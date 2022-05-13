class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int n = s.length();
        int len = 10, a= 4, aL= (int)Math.pow(a,len), h=0;
        if(len>= n)
            return new ArrayList();
        Set<Integer> seen = new HashSet();
        Set<String>res = new HashSet();
        Map<Character,Integer> m = new HashMap()
        {{ put('A',0); put('C',1); put('G',2); put('T',3); }};
        int[] num = new int[n];
        for(int i=0; i<n; i++)
            num[i] = m.get(s.charAt(i));
        for(int start=0; start< n-len+1; start++){
            if(start!=0)
                h = h*a - num[start-1] * aL + num[start+len-1];
            else
                for(int i=0; i< len; i++)
                    h = h*a +num[i];
            if(seen.contains(h))
                res.add(s.substring(start, start+len));
            seen.add(h);
        }
        return new ArrayList<String>(res);
    }
}