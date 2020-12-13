import os
import sys
import time


def main():
    day_str = os.getcwd().split('/')[-1].replace('day', '')

    try:
        module = __import__("main")

        print("Day " + day_str)

        part1 = measure_execution_time(module.main1)
        print("    Part 1: " + str(part1) + "s (" + str(round(part1 * 1000, 1)) + " ms)")

        part2 = measure_execution_time(module.main2)
        print("    Part 2: " + str(part2) + "s (" + str(round(part2 * 1000, 1)) + " ms)")
    except ModuleNotFoundError:
        return

def measure_execution_time(function):
    sys.stdout = open(os.devnull, "w")  # Prevent printing

    start_time = time.time()
    function()
    elapsed_time = time.time() - start_time

    sys.stdout = sys.__stdout__  # Restore printing

    return round(elapsed_time, 4)


if __name__ == "__main__":
    main()
