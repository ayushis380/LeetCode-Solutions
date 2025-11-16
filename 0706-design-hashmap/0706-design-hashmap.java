class MyHashMap {
    Map<Integer,Integer> m = new HashMap<Integer,Integer>();
    public MyHashMap() {
        
    }
    
    public void put(int key, int value) {
            m.put(key,value);
    }
    
    public int get(int key) {
        if(m.containsKey(key))
            return m.get(key);
        else
            return -1;
    }
    
    public void remove(int key) {
        if(m.containsKey(key))
            m.remove(key);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */