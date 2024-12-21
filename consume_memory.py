import time
import sys


times = int(sys.argv[1])


def perform(times):
    st = time.time()
    numbers = []
    for num in range(times):
        numbers.append(num)
        #time.sleep(0.00001)
    end = time.time()
    print(f'Took {end-st} seconds to generate {times} numbers.')


if __name__ == '__main__':
    perform(times)