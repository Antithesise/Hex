from threading import Lock
import sys

lock = Lock()

def print(*values, sep=' ', end='\n', file=sys.stdout, flush=False) -> str:
	"""print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)  
	Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments: file: a file-like object  
	(stream); defaults to the current sys.stdout. sep: string inserted between values, default a space. end: string  
	appended after the last value, default a newline. flush: whether to forcibly flush the stream.

	returns what is printed.
	"""

	with lock:
		file.write("\u001b[0m" + str(sep).join([str(v) for v in values]) + str(end) + "\u001b[0m")
		if flush:
			file.flush()
	
	return str(sep).join([str(v) for v in values]) + str(end)