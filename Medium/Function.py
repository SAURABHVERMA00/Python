def square(number):
    return number ** 2

def multiply(x,y):
    return x*y

result = square(5)
# print(result)
result2 = multiply(4,5)
result3 = multiply(x=4,y=5)
result4 = multiply('a',3)
result5 = multiply(5,'d')

# print(result2)
# print(result3)
# print(result4)
# print(result5)


import math
def circle_properties(r):
    area = (math.pi * r) * r
    circumference =( 2 * math.pi )* r
    return area, circumference

area, circumference = circle_properties(5)
# print(f"Area : {area:.2f}")
# print(f"Circumference : {circumference:.2f  }")


def greet(user="saur"):
    print(f"Hello {user}")

# greet()
# greet("Ankit")


# Lamda function
cube = lambda x,y: x**y
# print(cube(3,2))


#  *args fucntion
def sum_All(*args):
    total=0;
    for i in args:
        total+=i
    print(total)
    return sum(args)


# print(sum_All(1,2,3,4,5,6,7,8,9,10))

def generate_fun(limit):
    for i in range(2,limit+1,3):
        yield (i)

g=generate_fun(10)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in generate_fun(11):
#     # print(i)


# factorail number 

def factorial(n):
    if n==0 or n==1:
        return 1
    return factorial(n-1)+factorial(n-2)

f=factorial(3)
print(f)