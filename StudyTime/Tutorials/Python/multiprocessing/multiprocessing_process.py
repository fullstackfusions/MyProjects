import multiprocessing

def calculate_square(num):
    result = num * num
    print(result)

if __name__ == '__main__':
    processes = []

    for i in range(1, 6):
        process = multiprocessing.Process(target=calculate_square, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()