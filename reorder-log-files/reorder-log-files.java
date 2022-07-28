class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Comparator<String> comp = new Comparator<String>(){
            @Override
            public int compare(String s1, String s2){
                String[] arr1 = s1.split(" ",2);
                String[] arr2 = s2.split(" ",2);
                boolean digit1 = Character.isDigit(arr1[1].charAt(0));
                boolean digit2 = Character.isDigit(arr2[1].charAt(0));
                if(!digit1 && !digit2){
                    if(arr1[1].compareTo(arr2[1]) != 0)
                        return arr1[1].compareTo(arr2[1]);
                    else
                        return arr1[0].compareTo(arr2[0]);
                }
                else if(!digit1 && digit2){
                    return -1;
                }
                else if(digit1 && !digit2){
                    return 1;
                }
                else 
                    return 0;
                
            }
            
        };
        Arrays.sort(logs, comp);
        return logs;
    }
}