# We can pass functions as arguments to other functions:


def total_sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    else:
        return total


def square(x):
    return x*x


def cube(x):
    return x*x*x


num_to_calc = 3

print(f'Result square: {total_sum(num_to_calc, square)}')
print(f'Result cube: {total_sum(num_to_calc, cube)}')
