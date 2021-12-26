from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1
    d[b[i]] -= 1

for k in d:
    if d[k] != 0:
        print("NO")
        break
else:
    print("YES")
