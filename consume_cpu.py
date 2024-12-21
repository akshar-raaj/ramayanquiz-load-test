import time
import sys


times = int(sys.argv[1])


def perform(times):
    st = time.time()
    product = 1
    for _ in range(times):
        product = product * 1
    end = time.time()
    print(f'Took {end-st} seconds to repeat {times} times.')


if __name__ == '__main__':
    perform(times)
