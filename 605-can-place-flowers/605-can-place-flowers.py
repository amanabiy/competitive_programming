class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        """
        count = 0
        for i in range(len(flowerbed)):
            if i == 0:
                if i < len(flowerbed) - 1 and flowerbed[i + 1] == flowerbed[i] == 0:
                    count += 1
                    flowerbed[i] = 1
            if i == len(flowerbed) - 1:
                if flowerbed[i - 1] == flowerbed[i] == 0:
                    count += 1
                    flowerbed[i] = 1
            elif flowerbed[i + 1] == flowerbed[i - 1] ==  flowerbed[i] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n