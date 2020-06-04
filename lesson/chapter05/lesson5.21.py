def menu(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# menu(entree = 'beef', drink="coffee")

# ディクショナリー型でわかりやすい
d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'cake'
}
menu(**d)


