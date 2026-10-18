
# tuples are immutable
countreist=("Germany","France","Spain","Italy")
# in order to change tuple we have to change them to list first\
temp = list(countreist) # to change tuple to list 
temp.append("Belgium")
countreist=tuple(temp)
print(countreist)


# count -> to check occurance of something 

newcountry=countreist.index("Belgium")
print(newcountry)

# tuple
# tuple.index(element,start,end)