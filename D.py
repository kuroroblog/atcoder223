# 参考 ; https://docs.python.org/ja/3/library/heapq.html
from heapq import heappush, heappop

# 標準入力を受け付ける。
N, M = map(int, input().split())

# 有効グラフ情報を格納する。
edges = []
# →を指される数情報を格納する。
pointed_arrow_cnt = []
for i in range(0, N + 1):
    edges.append([])
    pointed_arrow_cnt.append(0)

for _ in range(M):
    a, b = map(int, input().split())

    edges[a].append(b)
    pointed_arrow_cnt[b] += 1

q = []

# 1からなのは、1~Nまでの値を利用しているため。
for i in range(1, N + 1):
    # →が指されていない番号を取り出して、ストックへ格納する。ストックの数列をソートする。
    if pointed_arrow_cnt[i] == 0:
        heappush(q, i)

ans = []
while len(q) != 0:
    # ストックの一番上を答えに移動する。
    p = heappop(q)
    ans.append(p)
    for to in edges[p]:
        # 答えに入れた値から生成される→を削除する。
        pointed_arrow_cnt[to] -= 1
        if pointed_arrow_cnt[to] == 0:
            # →が指されていない番号を取り出して、ストックへ格納する。ストックの数列をソートする。
            heappush(q, to)

if len(ans) == N:
    print(*ans)
else:
    print(-1)
