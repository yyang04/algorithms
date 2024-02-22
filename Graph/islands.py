from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def valid(i, j, grid, m, n):

            result = []
            for pos in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= pos[0] < m and 0 <= pos[1] < n and grid[pos[0]][pos[1]] == '1':
                    result.append(pos)
                    grid[pos[0]][pos[1]] = '0'
            return result

        def dfs(i, j, grid, m, n):
            for ni, nj in valid(i, j, grid, m, n):
                dfs(nj, nj, grid, m, n)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    count += 1
                    dfs(i, j, grid, m, n)
                    break

        return count




if __name__ == '__main__':
    solution = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    solution.numIslands(grid)
    print(grid)
