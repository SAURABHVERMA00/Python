def func(num):
    def func2(x):
        return x ** num
    return func2


myresult= func(2)
myresult(3)
print(myresult(3))