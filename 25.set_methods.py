set1={1,2,3,4,5,6}
set2={2,4,6,8,9}

# 1.to find the union of sets

print(set1.union(set2))

#2. to update the value of sets 

set1.update(set2) # set 1 ma lerayera set 2 merge gardinxa ani set 1 ma tyo value update hunxa 
print("value of updated set 1 ",set1)


# 
cities = {"Tokyo", "London", "Paris", "Kathmandu", "Dubai"}

countries = {"Japan", "Nepal", "France", "India", "Canada"}

citycountry=cities.union(countries)
print(citycountry)

# 
newcc=cities.update(countries) # new values wont be in newcc it will be added and updated in cities 


# 3. intersection

asian_countries = {"Nepal", "India", "China", "Japan", "Thailand","Russia"}

european_countries = {"France", "Germany", "Italy", "Spain", "Portugal","Russia"}

asian_countries.intersection_update(european_countries) # paila tyo intersection garxa ani tesma lagera update gardinxa 

print("updated asian countries",asian_countries) # updated asian countries {'Russia'}


# 4. symmetric difference means the value that is not common in two sets ,2 tai set ko print garxa 

odd = {1, 3, 5, 7, 9}

even = {1,2, 4, 6, 8, 10}

print("symmetric difference",odd.symmetric_difference(even)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# difference a-b or b-a if 2 set ma same no xa vane kattinxa 
# arko set ma na vako number print garauxa 

number=odd.difference(even)
number1=even.difference(odd)
print(number)
print(number1)


num1 = {1, 2, 3, 4, 5}
num2 = {1, 6, 7, 8, 9}

print(num1.difference(num2)) #{2, 3, 4, 5} 

#4. update difference 
# 5.symmetric difference update 

# 6.disjoint -> two sets with no common elements 
print(num1.isdisjoint(num2))# False because they have common elements which is one 

# 7. is superset -> to check if one set is super set of another set 
# if set a has all the elements of set b and even more elements then it is super set

# 8.issubset->to check if one set is sub set of another set 

# 9. remove -> to remove certain elements from a set ,if it doesnt find that element error will be returned 
a={1,2,3,4,5}
a.remove(5) #{1, 2, 3, 4}
print(a)

# 10.discard ->remove -> to remove certain elements from a set ,if it doesnt find that element no error will be returned 
# same as error 

# 11. pop -> it removes the random element from sets 

# 12. del -> it is used to completely remove the sets 

# 13.clear-> to empty all the elements from sets 