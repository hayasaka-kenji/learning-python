# datetime
import datetime

now = datetime.datetime.now()
print(now)

# IOSフォーマット
print(now.isoformat())

# フォーマット
print(now.strftime('%d/%m/%y-%H:%M:%S %f'))

# YYYY-MM-DD
today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

# 単位ごとで指定
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t.isoformat())
print(t.strftime('%d_%m_%y'))

# 計算して出力(1年前の出力)
print(now)
d = datetime.timedelta(days=365)
print(now - d)