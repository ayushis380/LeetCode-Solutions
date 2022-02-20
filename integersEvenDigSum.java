/* 2180. Count Integers With Even Digit Sum
[Easy]
*/
class Solution {
    public int countEven(int num) {
        int count =0; 
        for(int i = 1; i <= num; i++){
            if(check(i))
                count++;
         }
        return count;
    }
    public boolean check(int i){
        int sum = 0;
        while (i > 0){
        sum += i % 10;
        i /= 10;
        }
        return (sum % 2 == 0);
    }
}
