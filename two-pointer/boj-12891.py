# BOJ 12891 - DNA 비밀번호
import sys

S, P = map(int, sys.stdin.readline().split())
DNA = list(sys.stdin.readline().strip())
min_nums = list(map(int, sys.stdin.readline().split()))
ch = {'A':0, 'C':1, 'G':2, 'T':3}
count=0
for i in range(P):
    min_nums[ch[DNA[i]]]-=1
if not any(x > 0 for x in min_nums):
    count+=1

for i in range(P, S):
    min_nums[ch[DNA[i-P]]]+=1
    min_nums[ch[DNA[i]]]-=1
    if min_nums[ch[DNA[i]]]<=0:
        if not any(x > 0 for x in min_nums):
            count+=1
print(count)

## 시간 복잡도 : O(N)
## 배운 점: 
# 비교하는 문자의 수가 4개뿐이라 가능한 코드 
# 많아지면 전체배열을 검사하는 any와 같은 함수는 지양해야함(ex. 경계인 0보다 작아지는지 커지는지를 기준으로 개수를 센다거나 등)