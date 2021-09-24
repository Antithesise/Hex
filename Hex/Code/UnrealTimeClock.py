

# Typing
from typing import Callable

# Hex imports
from threading_print import print
from Htime import sleep

# System checks
from Checks import check
check()


# Definitions
def UnrealTimeClock(func: Callable) -> None:
	while func():
		sleep(1)
		print(end="\a", flush=True)
	
	return func()


# Runtime
if __name__ == "__main__":
	UnrealTimeClock(lambda: True)