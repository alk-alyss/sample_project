def subtract(a, b):
    return "POSITIVE" if a - b > 0 else "NEGATIVE"

import unittest

class SubtractTest(unittest.TestCase):
	def test_subtract(self):
		self.assertEqual(subtract(10, 5), "POSITIVE")
		self.assertEqual(subtract(5, 10), "NEGATIVE")

if __name__ == "__main__":
	unittest.main()

	result1 = subtract(10, 5)
	result2 = subtract(5, 10)
	print(result1)
	print(result2)