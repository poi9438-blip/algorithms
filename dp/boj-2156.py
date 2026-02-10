# BOJ 2156 - 포도주 시식
import sys
n = int(sys.stdin.readline())
wines = [int(sys.stdin.readline()) for _ in range(n)]

dp0 = wines[0]
if n>1: dp1 = wines[0] + wines[1]
if n>2: dp2 = max(dp1, wines[0]+wines[2], wines[1]+wines[2])

if n==1: 
    print(dp0)
    exit()
elif n==2: 
    print(dp1)
    exit()

for i in range(3,n):
    cur = max(dp2, dp1+wines[i], dp0+wines[i-1]+wines[i])
    dp0, dp1, dp2 = dp1, dp2, cur

print(dp2)

## 시간 복잡도 : O(n) (공간복잡도는 O(1))
## 배운 점: 
# - 자신이 포함 안되는 경우도 dp의 경우의 수에 포함시켜야 함
# - n이 작을 경우도 항상 고려하기