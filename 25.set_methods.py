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

even = {2, 4, 6, 8, 10}

print("symmetric difference",odd.symmetric_difference(even))