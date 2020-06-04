# 例外処理
l = [1, 2, 3,]
i = 5

try:
    () + l
except IndexError as exc:
    print('Dont worry: {}'.format(exc))
except NameError as exc:
    print(exc)
# 上記以外のエラーを取得する
except Exception as ex:
    print('other:{}'.format(ex))

print('last')