import time


def with_measure_time(func):
    start_time = time.time()
    response = func()
    end_time = time.time()
    measured_time = end_time - start_time
    return [measured_time, response]
