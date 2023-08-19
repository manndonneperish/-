fib = [1] * 30
for i in range(2, 30):
    fib[i] = fib[i - 2] + fib[i - 1]
print(list(fib))
