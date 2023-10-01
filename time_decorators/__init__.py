import time


def run_with_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} took {time.time() - start} seconds")
        return result
    return wrapper


def run_with_time_rec(func):
    def wrapper(*args, **kwargs):
        if wrapper.has_run:
            return func(*args, **kwargs)
        start = time.time()
        result = func(*args, **kwargs)
        wrapper.has_run = True
        print(f"Function {func.__name__} took {time.time() - start} seconds")
        return result
    wrapper.has_run = False
    return wrapper


def run_with_time_average(runs=10):
    def decorator(func):
        def wrapper(*args, **kwargs):
            counts = []
            for _ in range(runs):
                start = time.time()
                result = func(*args, **kwargs)
                counts.append(time.time() - start)
            print(
                f"Function {func.__name__} took an average of {sum(counts)/len(counts)} seconds")
            return result
        return wrapper
    return decorator


def run_with_time_rec_average(runs=10):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.has_run:
                return func(*args, **kwargs)
            counts = []
            for _ in range(runs):
                start = time.time()
                result = func(*args, **kwargs)
                counts.append(time.time() - start)
            wrapper.has_run = True
            print(
                f"Function {func.__name__} took an average of {sum(counts)/len(counts)} seconds")
            return result
        wrapper.has_run = False
        return wrapper
    return decorator
