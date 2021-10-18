# 標準入力を受け付ける。
S = input()

# 左シフトすることで、生成される文字列を格納する。
Slist = [S]
tmp = ''

# 左シフトのみを(0, 1, ..., N)回実行した場合に、生成される文字列を洗い出す。
for i in range(0, len(S)):
    tmp += S[i]
    Slist.append(S[i + 1:] + tmp)

# 生成された文字列を、辞書順でソートする。
Slist.sort()

# 辞書順でソートした文字列の、最小の文字列と最大の文字列を取得する。
min = Slist[0]
max = Slist[len(Slist) - 1]

print(min)
print(max)
