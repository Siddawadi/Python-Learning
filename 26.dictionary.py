# dictionary is a ordered collection of data that stores in key value pair 
# before python are unordered after python 3.7 it became ordered 

dic={
    "name":"harry",
    "yt":"codewithharry"
}

print(dic["name"])

# 1. to get all the keys of dictionary 

print(dic.keys())

# 2. to get all the values of dictionary 

print(dic.values())

# 3. to iterate all the values 

for i in dic.values():
    print(i)

# or it can be 
for i in dic:
   print(f"the value of {i} is {dic[i]}")


#    to get key and value in iteration 

for key,value in dic.items():
    print(f"{key}:{value}")
    

