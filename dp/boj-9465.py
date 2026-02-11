# BOJ 9465 - 스티커
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
   
    top0, bot0 = sticker[0][0], sticker[1][0]

    if n==1:
        print(max(top0, bot0))
        continue

    top1 = bot0+sticker[0][1]
    bot1 = top0+sticker[1][1]
    for i in range(2,n):
        new_top = max(bot0, bot1) + sticker[0][i]
        new_bot = max(top0, top1) + sticker[1][i]
        top0, bot0 = top1, bot1
        top1, bot1 = new_top, new_bot
    print(max(top1, bot1))

## 시간 복잡도 : O(T*n) (입력배열 제외하면 공간복잡도 O(1))
## 배운 점: 없음