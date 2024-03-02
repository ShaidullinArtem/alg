def is_prime(intt: int) -> bool:
	for i in range(2, intt):
		if intt//i == intt/i:
			return False
	else:
		return True


def main():
	print(is_prime(10))


if __name__ == '__main__':
	main()

