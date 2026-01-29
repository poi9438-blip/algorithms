# BOJ 2470 - 두 용액
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

left = 0
right = N-1
best = float('inf')
best_l = -1
best_r = -1

while left < right:
    current_sum = nums[left] + nums[right]
    if best > abs(current_sum):
        best = abs(current_sum)
        best_l = nums[left]
        best_r = nums[right]
    if current_sum > 0:
        right -= 1
    elif current_sum < 0:
        left += 1
    else: break
print(best_l, best_r)

## 시간 복잡도 : O(NlogN) 
## 배운 점: 포인터가 움직이려면 비교값의 부호를 유지해야함