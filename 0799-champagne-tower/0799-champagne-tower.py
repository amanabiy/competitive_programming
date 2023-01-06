class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        grid = [[0] * i for i in range(1, 102)]
        grid[0][0] = poured

        for row in range(len(grid) - 1):
            for col in range(len(grid[row])):
                rem = (grid[row][col] - 1) / 2
                if rem <= 0:
                    continue
                grid[row + 1][col] += rem
                grid[row + 1][col + 1] += rem

        return min(1, grid[query_row][query_glass])