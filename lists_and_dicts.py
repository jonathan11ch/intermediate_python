import math
import time
def run():
	my_list = [1, "hello", 4.5]
	my_dict = {"first_name": "jonathan", "last_name": "casas"}

	super_list = [
		{"first_name": "jonathan", "last_name": "casas"},
		{"first_name": "diego", "last_name": "casas"},
		{"first_name": "lina", "last_name": "bocanegra"}
	]

	super_dict = {
		"natural_nums" : [1,2,3,4,5],
		"integers" : [-1,-2,0,-1,-2],
		"floating" : [1.2, 4.5, 6.43]
	}


	for key, value in super_dict.items():
		print(key, "-", value)


if __name__=='__main__':
	run()
