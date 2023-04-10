from memory_profiler import profile, memory_usage
from src.printPrime import printPrime
import random
import timeit

@profile
def metriPrintPrime():
    printPrime(random.randrange(1,1000))


if __name__ == "__main__":
    execution_time = timeit.timeit(metriPrintPrime, number = 1)
    print(f"Execution time: {execution_time}")