# it is a combination of characters 

#  multi line string 

strr='''
this is a 
multi line string
'''
print(strr)


#  to access characters of a string 

name="Siddhartha Dawadi"

print(name[0]) # S

#  for looping through strings

for character in name :
    print(character,end=",")

#  to find length of string 
length = len(name)
print("length is ",length)

# string slicing

print(name[0:5]) # 0 index dekhi 5 index samma print garxa 
print("using :",name[:]) # prints the full array 

# - hune bittikai full len - tyo number 
print("using -3",name[0:-3]) # (name[0:len(name)-3]) so full length of array bata -3 hunxa
print("using -1:-3",name[-3:-1]) # name[len-3:len-1] so  [14-16] in betweeen print hunxa 



tutor = "Harry"
print("tutor",tutor[-4:-2]) #tutor[1] and tutor[2] in betweeen print hunxa 

#string as a array -> string is a sequence of characters 

