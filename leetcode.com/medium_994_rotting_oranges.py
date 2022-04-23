from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                cell = grid[r][c]
                if cell == 2:
                    q.append([r, c])
                elif cell == 1:
                    fresh += 1

        # print grid[0], '\n', grid[1], '\n', grid[2], '\n', time, fresh, '\n\n'
        while q and fresh > 0:

            for _ in range(len(q)):
                x, y = q.popleft()

                for xx, yy in [[x, y + 1], [x, y - 1], [x - 1, y], [x + 1, y]]:
                    if xx < 0 or xx > ROWS - 1:
                        continue
                    if yy < 0 or yy > COLS - 1:
                        continue
                    if grid[xx][yy] == 1:
                        grid[xx][yy] = 2
                        q.append([xx, yy])
                        fresh -= 1

            time += 1

            # print grid[0], '\n', grid[1], '\n', grid[2], '\n', time, fresh, '\n\n'

        return time if fresh == 0 else -1
