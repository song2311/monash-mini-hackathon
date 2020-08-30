import time

"""
    A decorator that wraps a function and calculates the time taken for the function to execute
    and writes/appends the time taken to the log file and all_times list
    Arguments:          all_times, the list of lapsed time calls
    Time complexity:    Best case = O(1) time complexity 
                        Worst case = O(1) time complexity 
    Return: the function decorator time_calls
"""
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