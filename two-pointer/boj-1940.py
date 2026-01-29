# BOJ 1940 - 주몽
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
start = 0
end = N-1
count = 0

while start < end:
    current_sum = nums[start] + nums[end]
    if current_sum == M:
        count += 1
        start += 1
        end -= 1
    elif current_sum > M:
        end -= 1
    else:
        start += 1
print(count)

## 시간 복잡도 : O(NlogN) => sort()때문에 더 느려짐
## 배운 점: 투포인터는 구간문제일 경우, 조합문제일 경우 각각 포인터의 시작위치가 달라진다