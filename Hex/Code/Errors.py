from typing import Iterable, Callable, Mapping, Tuple
from threading_print import print

class errors():
	def __init__(self, d: dict[str, str], lines: str) -> dict:
		"""
		Generates a dict of Python exceptions classes given a dict of the format {"ErrorName": "ErrorMessage"} 
		"""

		self.e: dict[str, Callable] = {}
		self.lines = lines

		def Err_init(self, func: Callable=exit, end: str="\n") -> None:
			print("\u001b[31m{self.msg}", flush=True, end=end)

			func()
		
		for k, v in d.items():
			self.e[k] = type(k, (Exception,), {"__init__": Err_init, "msg": v})
	
	def __add__(self, other: dict) -> "errors":
		self.e.update(other)

		return self
	
	def __sub__(self, other: list[str]) -> "errors":
		for k in other:
			self.e.pop(k)

		return self

	def __call__(self, err: str, lineno: int, end: str="\n"):
		print(f"\u001b[31mError on line {lineno}: {self.lines[lineno]}", end=end)
		return self.e[err](end)
