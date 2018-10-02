def fibonacci(position):
	if position == 1 or position == 2:
		return 1
	return fibonacci(position - 2) + 	fibonacci(position - 1)