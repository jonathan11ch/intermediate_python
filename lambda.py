
#Lambda function to detect palindromes

f = lambda string: string == string[::-1] 

print(f("ana"))
print(f("Jonathan"))

#High order functions

#Filter: Filter a list of number to choose only odd numbers

#List comprenhension approach
l = [i for i in range(11)]

odd = [i for i in l if i%2 !=0 ]

print(odd)


#filter approach
odd  = list(filter(lambda x: x%2 !=0, l))
print(odd)

#Map: apply a function(square function) to a list

#list comprehension approach

l = [1,2,3,4,5]

square = [i*i for i in l]
print(square)

#map approach
square = list(map(lambda x: x*x, l))
print(square)

#Reduce: multiply all elements of an array

#naive approach
sequence = [2, 2, 2, 2, 2, 2]
res = 1
for i in sequence:
	res = res*i

print(res)	

#reduce approach
from functools import reduce


res  = reduce(lambda x, y : x * y, sequence)
print(res)


