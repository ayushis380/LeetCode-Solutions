class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        timeMap = defaultdict(dict)

        # {   
        #     20: {'alice': {'mtv'}, 'bob': {'beijing'}}, 
        #     50: {'bob': {'mtv'}}
        #     }
        for trs in transactions:
            name, time, amount, city = trs.split(",")
            time = int(time)

            if name not in timeMap[time]:
                timeMap[time][name] = {city}
            else:
                timeMap[time][name].add(city)
        
        # for k, v in timeMap.items():
        #     print("key, ", k, " value is ", v)
        
        for trs in transactions:
            name, time, amount, city = trs.split(",")
            time = int(time)

            if int(amount) > 1000:
                invalid.append(trs)
                continue
            
            for t in range(time - 60, time + 60): # look for all other transactions within range
                if t not in timeMap:
                    continue
                if name not in timeMap[t]:
                    continue
                
                trsNameTime = timeMap[t][name] # dict for t and name
                # none of the checks above at 31 and 33 were true - so t and name have values in dict
                # check on length as if a time-name key has more than 1 value in dict - they must be invalid
                # eg 20: {'alice': {'mtv', 'beijing'}} or {'alice': {'mtv', 'mtv'}} - both are invalid, should be added to result

                if city not in trsNameTime or len(trsNameTime) > 1: # check on length as 
                    invalid.append(trs)
                    break
        
        return invalid
