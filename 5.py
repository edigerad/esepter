n = int(input())
k = int(input())
a = list(map(int, input().split()))
res = 0

# heap арқылы
# from heapq import heappop, heappush, heapify
# a = [-i for i in a]
# heapify(a)
# while k > 0:
#     t = heappop(a)
#     heappush(a, -((-t) // 2))
#     res += -t
#     k -= 1
# print(res)

# сұрыптау арқылы
# a.sort()
# while k > 0:
#     res += a[-1]
#     a.append(a.pop() // 2)
#     a.sort()
#     k -= 1
# print(res)

# list арқылы
# while k > 0:
#     res += max(a)
#     a.append(max(a) // 2)
#     a.remove(max(a))
#     k -= 1
# print(res)
