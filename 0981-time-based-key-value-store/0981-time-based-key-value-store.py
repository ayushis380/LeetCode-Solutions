class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ls = self.store[key]
        low, high = 0, len(ls) - 1
        result = ""

        while low <= high:
            mid = (low + high)//2
            if ls[mid][1] > timestamp:
                high = mid - 1
            else:
                result = ls[mid][0]
                low = mid + 1
        
        return result






# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)