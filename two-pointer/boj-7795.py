# BOJ 7795 - 먹을 것인가 먹힐 것인가
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A.sort()
    B.sort()

    count = 0
    j = 0
    for i in range(N):
        while j<M and A[i]>B[j]:
            j+=1
        count+=j
    print(count)
        
## 시간 복잡도 : O(NlogN)
## 배운 점: 배열이 두 개일 경우에도 투포인터의 방법은 크게 다르지 않다 + 조건에서는 범위검사부터 먼저