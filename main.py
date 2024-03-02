def is_prime(intt: int) -> bool:
	for i in range(2, intt):
		if intt//i == intt/i:
			return False
	else:
		return True


def number_sum(num: int) -> int:
	
	sum = 0
	for i in str(num):
		sum += int(i)
	
	return sum

def main():
	print(is_prime(10))
	print(number_sum(123))


if __name__ == '__main__':
	main()

