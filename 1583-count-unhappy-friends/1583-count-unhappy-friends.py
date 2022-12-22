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
        def findUnHappy(person, unhappy, betterOptions):
            for better in betterOptions[person]:
                if person in betterOptions[better]:
                    unhappy.add(better)
                    unhappy.add(person)

        unhappy = set()
        betterOptions = defaultdict(set)

        for person1, person2 in pairs:
            betterOptions[person1] = set(preferences[person1][:preferences[person1].index(person2)])
            betterOptions[person2] = set(preferences[person2][:preferences[person2].index(person1)])
            findUnHappy(person1, unhappy, betterOptions)
            findUnHappy(person2, unhappy, betterOptions)

        return len(unhappy)