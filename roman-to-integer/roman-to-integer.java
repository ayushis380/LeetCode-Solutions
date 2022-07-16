class Solution {
    public int romanToInt(String s) {
        int res =0;
        int len = s.length();
        for(int i=0; i< len; i++){
            if(i != len-1){
                if(s.charAt(i)== 'I' && s.charAt(i+1) == 'V'){
                    res+=4;
                    i++;
                    continue;
                }
                else if(s.charAt(i)== 'I' && s.charAt(i+1) == 'X'){
                    res+=9;
                    i++;
                    continue;
                }
                else if(s.charAt(i)== 'X' && s.charAt(i+1) == 'L'){
                    res+=40;
                    i++;
                    continue;
                }
                else if(s.charAt(i)== 'X' && s.charAt(i+1) == 'C'){
                    res+=90;
                    i++;
                    continue;
                }
                else if(s.charAt(i)== 'C' && s.charAt(i+1) == 'D'){
                    res+=400;
                    i++;
                    continue;
                }
                else if(s.charAt(i)== 'C' && s.charAt(i+1) == 'M'){
                    res+=900;
                    i++;
                    continue;
                }
            }
            if(s.charAt(i)== 'M')
                res+= 1000;
             else if(s.charAt(i)== 'D')
                res+= 500;
             else if(s.charAt(i)== 'C')
                res+= 100;
             else if(s.charAt(i)== 'L')
                res+= 50;
             else if(s.charAt(i)== 'X')
                res+= 10;
            else if(s.charAt(i)== 'V')
                res+= 5;
             else if(s.charAt(i)== 'I')
                res+= 1;
            
        }
        return res;
    }
}