from collections import Counter
import sys

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

print(round(sum(num_list)/n))

print(num_list[n//2])

mode = Counter(num_list).most_common()

if len(num_list) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])

print(max(num_list) - min(num_list))
