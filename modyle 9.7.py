def is_prime(func):

    def wrapper(*args):
        result = func(*args)
        sum_1 = sum(args)
        x = 0
        for i in range(2, sum_1 // 2 + 1):
            if sum_1 % i == 0:
                x = x + 1
        if x <= 0:
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime

def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
