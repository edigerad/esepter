def islands(grid):
    directions = ((1, 0), (0, -1), (-1, 0), (0, 1))

    def is_valid(x, y):
        if 0 <= x <= len(grid) - 1 and 0 <= y <= len(grid[0]) - 1:
            return grid[x][y] == '1'
        return False

    def bfs(i, j):
        if is_valid(i, j):
            grid[i][j] = '0'
            for direction in directions:
                bfs(i + direction[0], j + direction[1])

    res = 0
    for a in range(len(grid)):
        for b in range(len(grid[0])):
            if grid[a][b] == '1':
                res += 1
                bfs(a, b)
    return res


matrix = []
m, n = map(int, input().split())
for _ in range(n):
    matrix.append(input().split())
print(islands(matrix))
