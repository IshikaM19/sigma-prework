numbers = [2, 4, 1, 0, 2, -1]

def max_min_numbers(numbers):
    numbers.sort()
    print([numbers[0], numbers[-1]])

max_min_numbers(numbers)