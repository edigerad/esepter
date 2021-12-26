def rotate(matrix):
    n = len(matrix)
    k = []
    for _ in range(n):
        k.append([0] * n)

    c = n - 1
    for r in matrix:
        for w, e in enumerate(r):
            k[w][c] = e
        c -= 1
    for x in range(n):
        for y in range(n):
            matrix[x][y] = k[x][y]

    for q in range(n):
        print(' '.join(matrix[q]))


a = []
for i in range(int(input())):
    a.append(input().split())
rotate(a)
