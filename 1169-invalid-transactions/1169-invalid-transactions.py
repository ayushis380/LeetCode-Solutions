class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        timeMap = defaultdict(dict)
        invalid = []
        # {20 : { alice: {mtv} }, {50 : {alice: beijing}}

        for trs in transactions:
            name, time, amount, city = trs.split(",")
            time = int(time)

            if name not in timeMap[time]:
                timeMap[time][name] = {city} # new dict
            else:
                timeMap[time][name].add(city)
        
        for trs in transactions:
            name, time, amount, city = trs.split(",")
            time = int(time)
            amount = int(amount)

            if amount > 1000:
                invalid.append(trs)
                continue
            
            for t in range(time - 60, time + 60):
                if t not in timeMap:
                    continue
                if name not in timeMap[t]:
                    continue
                
                tname = timeMap[t][name]
                if city not in tname or len(tname) > 1:
                    invalid.append(trs)
                    break
            
        return invalid