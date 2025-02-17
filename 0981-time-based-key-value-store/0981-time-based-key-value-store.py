class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.store[key]
        low, high = 0, len(lst) - 1
        result = ""

        while low <= high:
            mid = low + (high - low)//2
            val, ts = lst[mid][0], lst[mid][1]
            if ts > timestamp:
                high = mid - 1
            else:
                result = val
                low = mid + 1
        
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)