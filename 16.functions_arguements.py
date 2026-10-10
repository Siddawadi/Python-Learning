
# !. Default Parameter

def average(a=10,b=20): 
    sum=a+b
    return sum 

t1=average() #30
t2=average(30,30) #60

# another way of passing arguements 

t3 = average(b=100,a=200) # yesto garesi order matter gardaina a ma 200  nai janxa 


# Arbitary Arguements
# 1. to create the list 

def sum(*Numbers): #it will create tuple 

    print(Numbers) #(20,) 

    print(type(Numbers)) #<class 'tuple'>

sum(20)

# wap to find multiplication using arbitary arguements
def multiplication(*input):
    result=1
    for i in input:
        result=result*i
    return result

        
mul=multiplication(4,5,6)
print("result is ",mul) # result is  120

# 2. to create the dict 

def dictt(**Input):
    print(Input)

dictt(no=21) #{'no': 21}
dictt(name="siddharth",roll=20) # {'name': 'siddharth', 'roll': 20}