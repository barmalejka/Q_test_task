from typing import List
from pprint import pprint


def num_islands(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    visited = set()
    islands = 0

    def bfs(r, c):
        '''Breadth-first search'''
        q = list()
        visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.pop()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:

                r, c = row + dr, col + dc

                if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == 1 and
                        (r, c) not in visited):

                    q.append((r, c))
                    visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands


if __name__ == '__main__':
    test_1 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
    ]

    test_2 = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
    ]

    test_3 = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
    ]

    print('Number of islands',num_islands(test_1))
    print('Number of islands',num_islands(test_2))
    print('Number of islands',num_islands(test_3))