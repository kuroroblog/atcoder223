# 標準入力を受け付ける。
N = int(input())

lines = []
endTime = 0
for _ in range(N):
    A, B = map(int, input().split())
    lines.append((A, B))
    endTime += A / B

# 導火線が完全消滅する時間を記録する。
# 片方(左 or 右)から火をつけて、導火線が完全消滅する時間 = ((A0 / B0) + (A1 / B1) + ... (AN / BN))
# 左右から火をつけて導火線が完全消滅する時間 = ((A0 / B0) + (A1 / B1) + ... (AN / BN)) / 2
endTime = endTime / 2

# 左からどのくらいの導火線の長さで、導火線が完全消滅するのか記録する。
leftLength = 0
for a, b in lines:
    # 導火線が完全消滅する時間よりも、a / bの時間が短い場合
    if a / b <= endTime:
        endTime -= a / b
        leftLength += a
    else:
        # 最後に残った時間分の長さを足し合わせる。
        # b * endTime : 導火線を燃やす速さ * 残り時間を足し合わせる。
        leftLength += b * endTime
        break

# 結果を出力する。
print(leftLength)
