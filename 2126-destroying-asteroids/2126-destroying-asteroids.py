class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        """
        """
        asteroids.sort(reverse=True)
        while asteroids:
            if asteroids[-1] <= mass:
                mass += asteroids[-1]
                asteroids.pop()
            else:
                return False
            
        return True