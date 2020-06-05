# 組み込み関数
ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

print(sorted(ranking, key=ranking.get))
# B,C,A 降順

print(sorted(ranking, key=ranking.get, reverse=True))
# B,C,A 昇順