# Example of starmap
from multiprocessing import Pool

def add(x, y):
    return x + y

if __name__ == "__main__":
    pairs = [(1, 2), (3, 4), (5, 6)]
    with Pool() as pool:
        result = pool.starmap(add, pairs)
    print(result)