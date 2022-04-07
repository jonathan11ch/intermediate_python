def read(path):
	number = []
	with open(path, "r", encoding = "utf-8") as f:
		number = [int(line) for line in f]

	return number


def write(path):
	names = ["jonathan", "nathalia", "diego", "lina"] 
	with open(path, "w", encoding = "utf-8") as f:
		for name in names:
			f.write(name)
			f.write("\n")
	



def run():
	print(read("./files/numbers.txt"))
	write("./files/names.txt")

if __name__ == '__main__':
	run()