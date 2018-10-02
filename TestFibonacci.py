from unitest import TestCase

class FibonacciTests(TestCase):
	def TestReturnsCorrectFibonacciNumber(self):
		correctSequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
		for index in range(len(correctSequence)):
			response = fibonacci(index)
			assert response = correctSequence[index]