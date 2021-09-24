t = int(input())

for _ in range(t):
    parenthesis = list(input())
    sum = 0

    for i in parenthesis:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")