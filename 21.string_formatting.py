letter=" Mr {} congratulations on winning {}"


print(letter.format("Siddharth","Champions League"))
#  Mr Siddharth congratulations on winning Champions League 


#  this is how the strings are formatted in the previous version of python 

#  After python 3.6

# we can use python f-strings to format string 


name="siddharth"
caste="dawadi"

price=200.9999
print(f"Mr {name} {caste}") # this is f string
print(f"the price of product is{price:.2f} ") # this will only take 200.99


# to create a string out of operations
a=5
b=2
c=50
print(f"{a*b+c}") #60

# if we dont want the values in string then 

print(f"the price of product is{{price:.2f}} ") 
# the price of product is{price:.2f} 