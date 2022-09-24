class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        """
        bfs starting from the id until you get to the level you  want and then get all           the movies and sort them with frequency
        """
        queue = deque([id])
        visited = [0] * len(friends)
        visited[id] = 1
        last_movies = defaultdict(int)
        
        while queue and level > 0:
            last_movies = defaultdict(int)

            for i in range(len(queue)):
                person = queue.popleft()

                for friend in friends[person]:
                    if not visited[friend]:
                        queue.append(friend)
                        visited[friend] = 1
            
            level -= 1
        
        for person in queue:
            for movie in watchedVideos[person]:
                last_movies[movie] += 1
        
        ans = list(last_movies.keys())
        ans.sort(key=lambda x: [last_movies[x], x])

        return ans