#  string methods 

# strings are immutable
# new string is formed 

# 1. to upper and lower case 

a="apple"
print(a.upper())
print(a.lower())

# 2. to strip or remove  unnecessary characters in string 

b='banana!,,,'
print(b.rstrip(",!"))

# 3. to replace
print(b.replace("banana!,,,","ball"))

#4.  to split

string1="siddharth dawadi"
str2 =string1.split(" ") #['siddharth', 'dawadi'] creates a new list
print(str2[0]) #siddharth

#5. to capitalize -> it makes sure that first character is capital and others are small

college="nccs"
teacher="aSHok"
sentence ="i study in nccs"


print(college.capitalize())
print(teacher.capitalize()) 
print(sentence.capitalize())

# 6.   center -> it takes string to center of as per the parameter  

print(college.center(20)) #         nccs        10 on one side and 10 on another length 

# 7.   count -> how many times is something repeating 

print(college.count("c")) #2

# 8. starts with and ends with 

print(college.startswith("n")) # true
print(college.endswith("s")) # true
print(sentence.endswith("nccs"))

# 9. find-> it searches the value and returns the first index and if not found then will return the first index 
letter = "1aaaaaaaaa"
Location ="I live in Kathmandu"
print(letter.find("a")) # 1
print(Location.find("Kathmandu"))

# 10.  index -> similar to find but it will return error when the searched entitiy is not found 

# 11. isalnum() -> to find our string is alpha numeric or not 

alphanum="alphanum1234"
print(alphanum.isalnum()) # return either true or false 

# 11.isUpper(), isLower() -> to check our string is in upper or in lower case 

# 12. isprintable -> it checks is our string is printable or not 
printabl="is this string printable \n"
print("is this printable",printabl.isprintable()) # false because we have escape sequence that won't be printed 

# 13. isspace()-> string white space hoki nai check garna 
Space=" "
print(" is it whitespace :",Space.isspace())

# 14. swapcase() -> changes uppercase to lower and lowercase to upper 
upp="THIS STRING IS IN UPPER case"
print("swapcase",upp.swapcase())

# 15. title -> this changes the strings into title 
country = "i live in nepal"
country1=country.title()
print(country.title()) # I Live In Nepal (first character capital banaidiyo )

print(country1.istitle()) # true