d = {'x': 100, 'y': '200'}

# # x y と出力される
# for v in d:
#     print(v)

# dict_items([('x', 100), ('y', '200')]) と出力される(タプルになっている。)
print(d.items())

# x  => 100 , y  => 200
for k, v in d.items():
    print(k, ' =>', v)

