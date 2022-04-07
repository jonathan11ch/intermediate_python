def palindrome(string):
	assert len(string) > 0, "Empty string is not allowed"
	return string == string[::-1]



def divisors(num):
	assert num > 0, "Must enter positive numbers"
	divisor_list = [n for n in range(1,num + 1) if num%n == 0]
	return divisor_list


print(divisors(-10))