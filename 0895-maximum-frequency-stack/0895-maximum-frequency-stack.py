class FreqStack:

    def __init__(self):
        self.freq = Counter() # store up to date freq of all elements
        self.group = defaultdict(list) # stores all frequencies seen by an element 
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.group[f].append(val) # eg 5 5 5, group will have g[1] = [5], g[2] = [5], g[3] = [5]. Every freq of element is updated in group
        
        if f > self.maxfreq:
            self.maxfreq = f

    def pop(self) -> int:
        res = self.group[self.maxfreq].pop()
        self.freq[res] -= 1
        if not self.group[self.maxfreq]: # if nothing left for key maxfreq then move to lower freq, as all freq are captured in group
            self.maxfreq -= 1
        
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()