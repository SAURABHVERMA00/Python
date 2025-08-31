tea=["Masla" , "Chai" , "Kashmiri Chai" , "Adrak Wali Chai" , "Elaichi Wali Chai"]

print(tea[1:3])

tea[3:4]="lemon"
print(tea,"\n")
# print(len(tea))

#  liSt comrehension
t=5
s=3
x=4
sqr=[x**3 for x in range(s,t)];
print(sqr)   