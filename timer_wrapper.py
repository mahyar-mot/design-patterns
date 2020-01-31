import time


def timing_wrapper(some_func):
    def wrapper():
        t1 = time.time()
        some_func()
        t2 = time.time()
        print("Time it takes to run the function: " + str(t2 - t1) + "\n")
    return wrapper

@timing_wrapper
def my_func():
    num_list = []
    for num in range(10000):
        num_list.append(num)
    print("\nSum of all the numbers: " + str(sum(num_list)))

my_func()
