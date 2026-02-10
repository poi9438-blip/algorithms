# BOJ 1149 - RGB거리
import sys
n = int(sys.stdin.readline())

prev = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    RGB = list(map(int, sys.stdin.readline().split()))
    ans = [0, 0, 0]
    for j in range(3):
        ans[j] = min(prev[j-1]+RGB[j], prev[(j+1)%3]+RGB[j])
    prev = ans
print(min(ans))

## 시간 복잡도 : O(n) (입력배열 제외하면 공간복잡도 O(1))
## 배운 점: 배열들이 같은 주소를 바라보고 있는지 체크하지 않으면 사이드이펙트 일어날 수 있음