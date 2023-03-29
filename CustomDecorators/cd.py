import os

import time
from colorama import Fore, Back, Style

# name:bool = Print time with function name
# rount_to:int = Round number to that
# function:func = Execute function when wrapped function was finished 
def get_time(name=False, round_to=2, function=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            t = time.time()
            result = func(*args, **kwargs)
            elapsed_time = time.time() - t
            if function:
                try:
                    function()
                except Exception as e:
                    print(Fore.RED + f"Error while executing function '{function}', {e}")
            if name:
                print(Fore.MAGENTA + f"Function '{func.__name__}' finished in {round(elapsed_time, round_to)} seconds" + Style.RESET_ALL)
            else:
                print(Fore.MAGENTA + f"Finished in {round(elapsed_time, round_to)} seconds" + Style.RESET_ALL)
            return result
        return wrapper
    return decorator

@get_time(name=True)
def example():
    time.sleep(1)