# Counter кітаптахана арқылы
# from collections import Counter
# s = Counter(input())
# for k in s:
#     print(k, s[k])

# defaultdict кітаптахана арқылы
# from collections import defaultdict
# s = defaultdict(int)
# for i in input():
#     s[i] += 1
# for k in s:
#     print(k, s[k])

# қарапайым сөздік арқылы
s = dict()
for i in input():
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
for k in s:
    print(k, s[k])
