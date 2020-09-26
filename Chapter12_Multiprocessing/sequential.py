import math
import time


def calc(num_elements):
    res = 0
    for i in range(num_elements):
        res += math.sqrt(i)
    print(res)


def main():
    start_time = time.perf_counter()

    for _ in range(4):
        calc(8_000_000)

    end_time = time.perf_counter()
    print("Took: {} s".format(end_time - start_time))


if __name__ == "__main__":
    main()
