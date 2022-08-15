class Solution {
    boolean seen;
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        boolean[] check = new boolean[n];
        HashSet<Integer>[] graph= new HashSet[n];
        
        for(int i=0; i< n ; i++){
            graph[i] = new HashSet<Integer>();
        }
        for(int[] e: edges){
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        if(graph[source].contains(destination))
            return true;
        
        seen = false;
        dfs(graph, check, source, destination);
        return seen;
        
        
    }
    public void dfs(HashSet<Integer>[] graph, boolean[] check, int source, int destination){
        if(!check[source] && !seen){
            // System.out.println("Source: " + source);
            if(source == destination){
                seen = true;
                return;
            }
        }
        check[source] = true;
        for(Integer neigh: graph[source]){
            if(!check[neigh])
                dfs(graph, check, neigh, destination);
        }
    }
}