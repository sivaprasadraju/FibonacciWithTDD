def fibonacci(number):
    FirstNumber = 0
    SecondNumber = 1
    count = 0
    FibonacciSeries = []

    if number < 0:
        raise ValueError('Input should be positive')

    elif number == 1:
        FibonacciSeries.append(FirstNumber)

    else:
        while count < number:
            FibonacciSeries.append(FirstNumber)
            nthNumber = FirstNumber + SecondNumber
            FirstNumber = SecondNumber
            SecondNumber = nthNumber
            count += 1

    return FibonacciSeries
