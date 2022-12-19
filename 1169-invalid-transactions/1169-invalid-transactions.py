class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        those who comes first considered first
        I also want to make them if they are in the 60 minute and different city add both to the invalid transaction
        Invalidity shoudl be a set because to avoid repetition
        
        does it considered fail if it contains both 1000 and also intersects with in the 60 min? should I just eliminate it or consider the otheer with in the 60 min range too?
        
        alice: [listOfTransactions]
        
        """
        trans = defaultdict(list)
        invalid = set()
        count = Counter(transactions)
        
        for i, tr in enumerate(transactions):
            name, time, score, place = tr.split(",")
            trans[name].append([int(time), int(score), place, i])
        
        for key in trans:
            data = trans[key]
            for i in data:
                if i[1] > 1000:
                    invalid.add(transactions[i[3]])
                for j in data:
                    if abs(i[0] - j[0]) <= 60 and i[2] != j[2]:
                        invalid.add(transactions[i[3]])
                        invalid.add(transactions[j[3]])
        ans = []
        for i in invalid:
            for _ in range(count[i]):
                ans.append(i)
        return ans
                    