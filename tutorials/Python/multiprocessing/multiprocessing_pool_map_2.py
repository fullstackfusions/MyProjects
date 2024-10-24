# Example of map:
from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with Pool() as pool:
        result = pool.map(square, numbers)
    print(result)