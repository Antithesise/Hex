from threading_print import print

def UnrealTimeClock(func):
	from Htime import sleep
	while func():
		sleep(1)
		print(end="\a", flush=True)

if __name__ == "__main__":
	UnrealTimeClock(lambda: True)