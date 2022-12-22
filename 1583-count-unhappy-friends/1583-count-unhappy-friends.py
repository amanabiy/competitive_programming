class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        What I would do is save this
        n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
        {
          1: {2}
          3: {0, 2}
          2: {1,3}
          0: {1,3}
        }
        """
        def findBetterFriends(pref, pairedWith):
            better = set()
            for i in pref:
                if i == pairedWith:
                    break
                better.add(i)
            return better
        
        def findUnHappy(betterOpt, person, unhappy):
            for better in betterOpt:
                if person in betterOptions[better]:
                    unhappy.add(better)
                    unhappy.add(person)
        
        unhappy = set()
        betterOptions = defaultdict(set)

        for person1, person2 in pairs:
            betterOptions[person1] = findBetterFriends(preferences[person1], person2)
            betterOptions[person2] = findBetterFriends(preferences[person2], person1)
            
            findUnHappy(betterOptions[person1], person1, unhappy)
            findUnHappy(betterOptions[person2], person2, unhappy)
        
        return len(unhappy)
            
            