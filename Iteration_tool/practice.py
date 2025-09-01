f=open('Iteration_tool/saurabh.py')
# print(f.readline())
# f.close()


# for line in f:
#     print(line)

# while True:
#     line=f.readline();
#     if not line:
#         break;
#     print(line,end="\n");


list =[1,2,3,4,5]
I=iter(list)
print(I.__next__())
print(I.__next__())