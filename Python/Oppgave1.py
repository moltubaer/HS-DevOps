def func(num1, num2):
    prod = num1 * num2
    if prod <= 1000:
        return prod
    else:
        return num1 + num2


result = func(20, 30)
print("The result is", result)

result = func(40, 30)
print("The result is", result)

