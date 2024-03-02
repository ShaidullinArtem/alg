

def number_sum(num: int) -> int:
	
	sum = 0
	for i in str(num):
		sum += int(i)
	
	return sum

def main():
	print(number_sum(123))


if __name__ == '__main__':
	main()

