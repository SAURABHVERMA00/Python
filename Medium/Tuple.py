chai_type= ( "Masala Chai", "Adrak Chai", "Elaichi Chai" )  # tuple
print(chai_type[-1])  # accessing items
print(len(chai_type))  # length of tuple

more= ( "Lemon Chai", "Kashmiri Chai" )

newChai=chai_type + more
print(newChai)


(a,b) =more
print(a)
print(b)    

print(type(newChai))  # it will return tuple

chai=("" , (), (1,2,3))
print(chai[2][1])