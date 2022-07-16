class Solution {
    public int myAtoi(String s) {
        int res=0;
        int sign =1;
        int len = s.length(), i=0;
        if(len == 0)
            return 0;
        while(i< len && s.charAt(i) == ' '){
            i++;
        }
        if(i< len && s.charAt(i) == '-'){
            sign =-1;
            i++;
        }else if(i<len && s.charAt(i) == '+'){
            sign =1;
            i++;
        }
        while(i< len && Character.isDigit(s.charAt(i))){
            int val = s.charAt(i) -'0';
            if((res > Integer.MAX_VALUE/10) || (res == Integer.MAX_VALUE/10 && val > Integer.MAX_VALUE% 10)){
                return (sign == 1) ? Integer.MAX_VALUE: Integer.MIN_VALUE;
            }
            res = res* 10 +val;
            i++;
        }
            return sign * res;
    }
}