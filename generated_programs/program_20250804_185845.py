# Decorator Example (2025-08-04 18:58:45)
def timer(func):
    import time
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

print("5! =", factorial(5))
