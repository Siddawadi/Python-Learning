# set is a unordered collection of data types that can't have repeated elements 
# it is used if we want to collect data that can't be repeated

# for eg the emp id that has already been listed in db 
# x order matter gardaina so unordered
# they immutable 

s={2,3,4,5,6,6} # {2, 3, 4, 5, 6} 6 is not repeated 
print(s)

#1. to create a empty set 

# we can't use {} as it will become dictionary

name={}
print(type(name)) # <class 'dict'> it will be dictionary or dict

# so
newset=set()
print(type(newset)) # <class 'set'>


# 2. To access items in set -> use for loop 

students={"sid","krish","harry","subin"}

for i in students:
    print(i,end=" ") # sid subin krish harry 