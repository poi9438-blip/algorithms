# BOJ 10844 - 쉬운 계단 수
import sys
N = int(sys.stdin.readline())
MOD = 1000000000

prev = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1,N):
    curr = [0] * 10
    curr[0] = prev[1]
    curr[9] = prev[8]
    for j in range(1,9):
        curr[j] = (prev[j-1] + prev[j+1])%MOD
    prev = curr
        
print(sum(prev)%MOD)

## 시간 복잡도 : O(N) (공간복잡도는 O(1))
## 배운 점: 
# - DP는 재사용하는 범위에 따라 공간복잡도를 줄일 수 있다
# - 아직은 점화식을 세우는게 어려움 연습하자!