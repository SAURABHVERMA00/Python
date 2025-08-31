chai_types={"first":"Masala Chai" , "second":"Lemon Chai" , "third":"Kashmiri Chai"}

#  accessing items
# print(chai_types["second"]);
# print(chai_types["thir])   #it get error if key is not present
# print(chai_types.get("third"))  # it will return none if key is not present
# print(chai_types.get("fourth","saurabh"))  # it will return Not Found if key is not present


chai_types["fourth"]="Adrak Wali Chai"  # adding new key value pair
# print(chai_types)

for key in chai_types:
    print(key,end=":")
    print(chai_types.get(key), end=",");

print(end="\n")

output=[]

#  if you dont want to make other print 
for key , value in chai_types.items():
    output.append(f"{key}:{value}") # f means formatted string literal


print(",".join(output))


if("first") in chai_types:
    print("yes first is present")
else:
    print("no first is not present")

print(len(chai_types))  # length of dictionary

# multidemensional dictionary
my_family={
    "child1":{
        "name":"saurabh",
        "year":2002
    },
    "child2":{
        "name":"shubham",
        "year":2005
    },
    "child3":{
        "name":"shivam",
        "year":2010
    }
}

print(my_family.get("child3").get("name"))

print(my_family["child1"]["year"])

# comprenhension

sq={x:x**2 for x in range(7)}
print(sq)


#  if you want to create dicotnary from lit
lst=["saurabh" , "shubham" , "shivam"]
num="deliciuos"

dictonary=dict.fromkeys(lst , num)
print(dictonary)