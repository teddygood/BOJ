import sys
import heapq

n = int(input())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(q)[1])