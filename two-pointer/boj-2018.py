# BOJ 2018 - 수들의 합 5
import sys
N = int(sys.stdin.readline())

left = 1
current_sum = 0
count = 0

for right in range(1, N + 1):
    current_sum += right

    while current_sum > N:
        current_sum -= left
        left += 1

    if current_sum == N:
        count += 1
        
print(count)

## 시간 복잡도 : O(N)
## 배운 점: 
# - 투포인터 코드를 더 직관적으로 개선
# - 슬라이딩 윈도우는 구간의 크기가 고정되어 있을 경우에 사용한다