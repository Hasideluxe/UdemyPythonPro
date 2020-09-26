import math
import time
from multiprocessing import Process


NUM_PROCESSES = 4


def calc(num_elements):
    res = 0
    for i in range(num_elements):
        res += math.sqrt(i)
    print(res)


def main():
    processes = []

    for _ in range(NUM_PROCESSES):
        processes.append(Process(target=calc, args=[8_000_000]))

    start_time = time.perf_counter()

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_time = time.perf_counter()
    print("Took: {} s".format(end_time - start_time))


if __name__ == "__main__":
    main()
