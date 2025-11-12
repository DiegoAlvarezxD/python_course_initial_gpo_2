def fibonacci(limite: int):
    """Serie de fibonacci con generadores"""
    a, b = 0, 1
    for num in range(limite):
        yield a
        a, b = b, a + b
        
for num in fibonacci(50):
    print(num)