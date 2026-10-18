
# 1.Append->  to add new elements on the end of the list 
l=[1,2,3,4,5]
l.append(6)
print(l)

# 2.Sort

a=[3,4,2,6,1,6,3,8]
a.sort() # for ascending order

a.sort(reverse=True) # descending order
print(a)

print("a is :\t",a)

# 3. Index ->prints the index of 1st elements it finds 
print(a.index(4))

# 4. copy 
b=a
# when we change b then a is also changed because b holds the reference of a 
# thats why we must use copy function 

b=a.copy()
print("copied b is ",b) # copied b is  [8, 6, 6, 4, 3, 3, 2, 1]
b[0]=0
print("changed b is ",b) #[0, 6, 6, 4, 3, 3, 2, 1]

# 5. count
print(b.count(6))

#6. insert -> a.insert(index,number) doesnt replace just inserts 
b.insert(1,4)
print(b)


# 7.extend -> used to concat two lists
x=[1,2,3]
y=[7,8,9]
x.extend(y) # x ra y concat garna 
print("x is ",x)

# 8. pop 
l=[10,20,30,40] 
length=len(l)
l.pop(length-1)
print("pop example",l)

# another way of concatinating two lists 

k = x+y
print("x+y =",k)