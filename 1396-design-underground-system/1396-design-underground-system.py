class UndergroundSystem:

    def __init__(self):
        self.travel = defaultdict(list)
        self.person = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.person[id].append(stationName)
        self.person[id].append(t)
        # print(self.person[id])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.person[id][0]
        startTime = self.person[id][1]
        del self.person[id]
        travelTime = t - startTime
        key = start + "," + stationName

        self.travel[key].append(travelTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + "," + endStation
        total = sum(self.travel[key])
        length = len(self.travel[key])

        return total/length




# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)