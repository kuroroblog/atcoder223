# 標準入力を受け付ける。
X = int(input())

# Xの値が100より小さいならば、`No`にする。
if X < 100:
    print('No')
    exit()

# Xの値を100で割った余りを取得する。
amari = X % 100

# 余りが0の場合、`Yes`, そうでない場合`No`と出力する。
if amari == 0:
    print('Yes')
else:
    print('No')
