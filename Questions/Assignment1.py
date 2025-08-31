# Age group categories
# age= int(input("Enter your age : \n"));

# if age<13 :
#     print("You are a Child")
# elif(age>=13 and age<=19):
#     print("You are a Teenager")
# elif(age>19 and age<=59):
#     print("You are an Adult")
# else:
#     print("You are a Senior Citizen")



# 2 : Movie ticket 

# age= int(input("Enter your age : \n"));
# day =input("Enter the day : \n");


# price = 12 if age>=18 else 8 
# price= price if day!="wednesday" else price-2;
# if(age<18):
#     if(day=="wednesday"):
#         print("Your ticket price is $",price)
#     else:
#         print("Your ticket price is $",price)
# else:
#     if(day=="wednesday"):
#         print("Your ticket price is $",price)
#     else:
#         print("Your ticket price is $",price)


#3 Leap Year 

year= int(input("Enter the year : \n"));

if( (year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0)):
    print(year , " is a leap year")
else:
    print(year , " is not a leap year")