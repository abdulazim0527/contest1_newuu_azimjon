import time
import random

def decorator_1(func):
    def wrapper(*argumentlar1, **event1):
        boshlangich_time = time.time()  # Record the start time
        rezultat = func(*argumentlar1, **event1)  # Call the original function
        tugash_time = time.time()  # Record the end time
        execute_time = tugash_time - boshlangich_time  # Calculate execution time
        print(f"{func.__name__} call executed in {execute_time:.7f} sec")  # Print execution time
        return rezultat  # Return the result of the original function
    return wrapper

@decorator_1
def func():
    print("Qani boshladik!")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)

@decorator_1
def funx(n=2, m=5):
    print("Keyingisiga navbat!")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()
