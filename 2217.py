n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(n):
    rope.append(rope[n]*(n+1))
