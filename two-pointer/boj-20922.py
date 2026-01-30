# BOJ 20922 - 겹치는 건 싫어
import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())
nums = sys.stdin.readline().split()

cnt = defaultdict(int)
left = 0
max_length = 0

for right in range(N):
    cnt[nums[right]] += 1
    
    while cnt[nums[right]] > K:
        cnt[nums[left]] -= 1
        left+=1

    max_length = max(max_length, right-left+1)

print(max_length)


## 시간 복잡도 : O(N)
## 배운 점: 조건문을 만들 때는 항상 거기에 속하지 않는 경우를 고려할 것