n = int(input())

mod = 1000000
p = mod//10*15

fibo = [0, 1]

for i in range(2, p):
    fibo.append(fibo[i-1] + fibo[i-2])
    fibo[i] %= mod
print(fibo[n % p])

a, b = 0, 1
for _ in range(n):
    a, b = b%mod, (a+b) % mod

print()