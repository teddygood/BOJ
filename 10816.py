from sys import stdin

# _ = stdin.readline()
n = sorted(map(int,stdin.readline().split()))
# _ = stdin.readline()
m = map(int,stdin.readline().split())

def binary(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return mid

n_dic = {}
for n in n:
    start = 0
    end = len(n) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, n, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in m))