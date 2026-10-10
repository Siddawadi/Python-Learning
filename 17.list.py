list=[1,2,3,4,5,6]

sum =0
for i in list:
    sum=sum+i

print('this is the sum ',sum)

list1=["red","green","blue","yellow"]

# to check  is yellow present in list 1 then ?

if "yellow" in list1: # yellow is present
    print("yellow is present")

else:
    print("yellow isn't present")


numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[0:9:1] , end=" " "\n") #[1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(numbers[0:9:2] , end=" ""\n") # 1, 3, 5, 7, 9] 
print(numbers[0:9:3] , end=" ""\n")


# list comprehension => used for creating a new list from other iteratives like lists tuples 
#  dict etc

newlist=[i for i in numbers]
newlist11=[i*i for i in numbers]
print("new list is created ",newlist)
print("new list is created i*i ",newlist11)

# lets do list comprehension with conditions 

arr=[i for i in range(0,10) if(i%2==0)]
print("conditional list comprehension ",arr)