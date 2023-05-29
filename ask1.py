def subtract(a, b):
    return "POSITIVE" if a - b > 0 else "NEGATIVE"

if __name__ == "__main__":
	result1 = subtract(10, 5)
	result2 = subtract(5, 10)
	print(result1)
	print(result2)