# BOJ 1806 - 부분합
import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

left = 0
current_sum = 0
min_length = float('inf')
for right in range(N):
    current_sum += nums[right]
    while current_sum >= S:
        length = right-left+1
        if min_length > length:
            min_length = length
        current_sum -= nums[left]
        left += 1

if min_length != float('inf'):
    print(min_length)
else:
    print(0)

## 시간 복잡도 : O(N)
## 배운 점: 실수를 줄이기 위해 문제의 요구사항을 정리하고 문제를 풀자