# デフォルト引数
def menu(entree='beef', drink='soda', dessert='cake'):
    print('entree =>', entree)
    print('drink =>', drink)
    print('dessert =>', dessert)


menu(entree='chicken')
# entree => chicken
# drink => soda
# dessert => cake

# 位置引数を間違えるとエラーになる
# TypeError: menu() got multiple values for argument 'entree'
menu('beer', entree='chicken')