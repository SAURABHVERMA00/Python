# count positive number 

# n= int(input("Enter the number of elements : \n"));
# list=[];
# for i in range(0,n):
#     ele=int(input("enter the element : \n"));
#     list.append(ele);

# count=0;

# for i in list:
#     if(i>=0):
#         count+=1;

# print("The list is : ",list);
# print("The count of positive numbers is : ",count);

sum=0

# for i in list:
#     if(i%2==0):
#         sum+=i;

# print("The sum of even numbers is : ",sum);

# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i*2)


# // reverse a string 

# str=str(input("Enter the string : \n"));

# rev=""

# for i in str:
#     rev = i+rev;

# print("The reverse string is : ",rev);


# for i in str:
#     if(str.count(i) ==1 ):
#         print(i);
#         break;


# factorial number 

# n= int (input("Enter the number : \n"));

# fact=1;
# while (n > 0):
#     fact=fact *n;
#     n=n-1;

# print("The factorial is : ",fact);
# num=True;
# while(True):
#     if(n >= 1 and n <=10):
#         print("The number is between 1 to 100");
#         num=False;
#         break;
#     else:
#         n= int (input("Enter the number again : \n"));


# is_prime=True;

# if n >1 :
#     for i in range(2,n):
#         if (n % i ) ==0:
#             is_prime=False;
#             break;


# if is_prime:
#     print(n , " is a prime number");
# else:
#     print(n , " is not a prime number");

#unique element

item=["banana" , "mango" , "apple" , "orange" , "banana"]

unique_item=set();

# for i in item:
#     if i in unique_item:
#         print(i , " is a duplicate item"); 
#         break;
    

#     unique_item.add(i);


# BACKOFF ALGORITHM

import time

wait_time=1;
attempts=0;
max_reattempt=5;


while(True):
    print("Attempts : ",attempts +1 , "wait time : " , wait_time)
    time.sleep(wait_time);
    attempts+=1;
    wait_time *=2;
    if(attempts == max_reattempt):
        print("Max attempts reached");
        break;

