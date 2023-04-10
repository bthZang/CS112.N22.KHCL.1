from memory_profiler import profile, memory_usage
from src.checkTriangle import checkTriangle
import random
import timeit


@profile
def metricCheckTriangle():
    checkTriangle(
        random.randrange(1, 3000), random.randrange(1, 3000), random.randrange(1, 3000)
    )


if __name__ == "__main__":
    execution_time = timeit.timeit(metricCheckTriangle, number=1)
    print(f"Execution time: {execution_time}")
    # memory_usage_result = max(memory_usage((profFindNextDate)))
    # print(f"Memory usage: {memory_usage_result}")