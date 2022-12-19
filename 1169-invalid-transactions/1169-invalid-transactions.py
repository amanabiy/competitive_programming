class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        those who comes first considered first
        I also want to make them if they are in the 60 minute and different city add both to the invalid transaction
        Invalidity shoudl be a set because to avoid repetition
        
        does it considered fail if it contains both 1000 and also intersects with in the 60 min? should I just eliminate it or consider the otheer with in the 60 min range too?
        
        alice: [listOfTransactions]
        
        """
        trans = defaultdict(dict)
        invalid = set()
        
        for data in transactions:
            name, time, amount, place = data.split(",")
            time = int(time)
            if time not in trans:
                trans[name][time] = {place}
            else:
                trans[name][time].add(place)
        
        for i, data in enumerate(transactions):
            name, time, amount, place = data.split(",")
            time = int(time)
            if int(amount) > 1000:
                invalid.add(i)
                continue

            for t in range(time - 60, time + 61):
                if t in trans[name] and (place not in trans[name][t] or len(trans[name][t]) > 1):
                    invalid.add(i)
        
        return [transactions[i] for i in invalid]