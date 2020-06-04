def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)
#
# # 順序を正しく入れないと期待していない結果になる
menu('beef', 'soda', 'cake')
print('----')

# キーワードアーギュメント・キーワード引数
menu(entree= 'beef', drink='soda', dessert='cake')
print('----')


# 混ぜてつかうことも可能
menu('beef', drink='soda', dessert='cake')
print('----')

# 混ぜて使うこともできるが位置引数を間違えるとエラーになる
# menu(drink='soda', 'beef', dessert='cake')