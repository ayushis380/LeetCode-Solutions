class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        boolean[] check = new boolean[n];
        HashSet<Integer>[] graph = new HashSet[n];
        
        for(int i=0; i<n; i++){
            graph[i] = new HashSet<Integer>();
        }
        for(int[] edge : edges){
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        if(graph[source].contains(destination)){
            return true;
        }
        check[source] = true; 
        int curr;
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(source);
        while(!q.isEmpty()){
            curr = q.poll();
            if(curr == destination)
                return true;
            for(Integer neigh: graph[curr]){
                if(!check[neigh]){
                    q.offer(neigh);
                    check[neigh] = true;
                }
            }
        }
        return false;
        
    }
}