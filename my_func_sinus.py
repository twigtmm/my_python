def fun(x):
    import math
    return math.sin(x)

x=float(input("Введите число: "))
if 0.2<=x<=0.9:
    print(fun(x))
else:
    print("1")
