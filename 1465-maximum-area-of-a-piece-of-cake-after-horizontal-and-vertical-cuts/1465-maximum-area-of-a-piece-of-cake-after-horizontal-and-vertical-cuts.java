class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        int hlen = horizontalCuts.length;
        int vlen = verticalCuts.length;
        int hmax=0, vmax=0;
        
        Arrays.sort(verticalCuts);
        Arrays.sort(horizontalCuts);
        // if(hlen ==1 ){
            hmax = Math.max(horizontalCuts[0], h-horizontalCuts[hlen-1]);
        // }
        // if(vlen ==1 ){
            vmax = Math.max(verticalCuts[0], w-verticalCuts[vlen-1]);
        // }
        for(int i=0; i< hlen-1; i++){
            hmax = Math.max(hmax, horizontalCuts[i+1] - horizontalCuts[i]);
        }
        for(int i=0; i< vlen-1; i++){
            vmax = Math.max(vmax, verticalCuts[i+1] - verticalCuts[i]);
        }
        // System.out.println(hmax);
        // System.out.println(vmax);
        // System.out.println(hmax * vmax);
        // long temp = hmax*vmax % 1000000007;
        // System.out.println(temp);
        // return (int)(temp);
        return (int)((long)hmax * vmax % 1000000007);
            
        
    }
}