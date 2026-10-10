# a container to store some sort of data 

# types of data types 

# 1. Numerical :int,Float,Complex
# a int
a=1
b=3
c=a+b

print(a+b)
str ="hello"
print("the type of c1 is " , type(c))

# b float
a1=1.1
b1=2.2
c1=a1+b1
print("the type of c1 is " , type(c1))

# c complex
complexnumb = complex(9,10) # // (9+10j)
print(complexnumb)

# boolean
x=True
print(x)


# 2. Text datatype:string

# 3. sequence data :list and tuple
# list is a collection of data with elements , it is muttable 
# tuple exactly list but it is immutable 

list1=[8,9,10,[11,12]]
print(list1[3][0]) # 11

tuple=(("parrot","pigeon"),("cat","dog","zebra"))
print(tuple[0][0]) # parrot

# 4. Mapped data type : dict
# dict -> it is a data type which stores data in key value pair 
dict1={
    { "name":"sid","course":"bca","semester":"6th"},
     { "name":"aayush","course":"bim","semester":"6th"},


}