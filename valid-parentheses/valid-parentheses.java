class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        Map<Character, Character> m = new HashMap<>();
        m.put('}','{');
        m.put(')','(');
        m.put(']','[');
        for(int i=0; i< s.length(); i++){
            char ch = s.charAt(i);
            if(m.containsKey(ch)){
                char topVal = st.isEmpty() ? '!' : st.pop();
                if(topVal != m.get(ch))
                    return false;
            }
            else
                st.push(ch);
        }
        return st.isEmpty();
    }
}