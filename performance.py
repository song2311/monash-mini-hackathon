import time

def decorator(all_times):
    def time_calls(func):
        def helper(*args, **kwargs):
            file = open("log.txt", 'a+')
            start = time.time()
            method = func(*args, **kwargs)
            end = time.time()
            all_times.append((end-start)*1000)
            file.write("Elapsed time of %s in milliseconds : %f\n" %(func.__name__, (end-start) * 1000))
            file.close()
            return method
        return helper
    return time_calls