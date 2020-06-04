def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

ca1 = circle_area_func(3)
ca2 = circle_area_func(3.14)

print(ca1(10))
# 300
print(ca2(10))
# 314