# BOJ 2003 - 수들의 합 2
import sys

N, M = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
current_sum = 0
count = 0

while True:
    # 현재 합이 목표 이상이면
    # left를 줄여서 구간을 축소
    if current_sum>=M:
        if current_sum == M :
            count+=1
        current_sum-=l[left]
        left+=1

    # 현재 합이 목표보다 작으면
    # right를 늘려서 구간을 늘림
    elif current_sum<M:
        if right==N: break
        current_sum+=l[right]
        right+=1
print(count)

## 시간 복잡도 : O(N)
## 배운 점: 투 포인터라고 무조건 정렬X