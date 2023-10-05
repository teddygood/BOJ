n, m = list(map(int, input().split(' ')))

arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        # 잘랐을 때 양 계산
        if x > mid:
            total += x - mid

    # 부족한 경우 더 많이 자르기
    if total < m:
        end = mid - 1
    # 충분한 경우 덜 자르기
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답
        start = mid + 1

print(result)