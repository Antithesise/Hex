from typing import Iterable, Callable, Mapping, Tuple
from threading_print import print


# Definitions
class errors():
	def __init__(self, d: dict[str, str], lines: str="") -> dict:
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

	def __or__(self, other: str) -> "errors":
		self.lines = other

		return self

	def __call__(self, err: str, lineno: int, end: str="\n"):
		print(f"\u001b[31mError on line {lineno}: {self.lines[lineno]}", end=end)

		return self.e[err](end)


# Runtime
e = errors({
	"!": "+++!!!!!+++", # Exception
	"?": "+++?????+++", # Warning
	"Address": "+++ Error At Address: 14, Treacle Mine Road, Ankh-Morpork +++ Please Reinstall Universe And Reboot", # LookupError/KeyError/FileNotFoundError/FileExistsError/ModuleNotFoundError
	"Cheese": "+++ Out Of Cheese Error +++ Redo From Start", # TimeoutError/MemoryError
	"Soon":"+++ Cominge Soon To A Pt Nr. You +++ Request Banged Grains And Install When Cooked", # NotImplementedError
	"Cucumber": "+++ Divide By Cucumber Error +++ Please Reinstall Universe And Reboot", # ZeroDivisionError
	"Data": "+++ Insufficient Data +++ Redo From Start", # TypeError
	"Domain": "+++ Eternal Domain Error +++ Redo From Start", # OSError
	"Jelly": "+++ Mr. Jelly! Mr. Jelly! +++ Redo From Start", # SystemError
	"Melon": "+++ MELON MELON MELON +++ Redo From Start", # ValueError/NameError
	"Mine": "\nMine! Waah!", # FileNotFoundError (.FTB only)
	"Mum": "+++ Hi Mum Is Testing +++ Redo From Start", # SyntaxError
	"One": "+++ Oneoneoneoneoneone +++ Redo From Start", # ArithmeticError
	"Shrimp": "+++ Millenium Hand And Shrimp +++ Evaluation Interrupted", # KeyboardInterrupt
	"Temp": "+++ Empty Temp Error +++ Redo From Start", # ReferenceError
	"Whoops": "+++ Whoops! Here Comes the Cheese! +++ Redo From Start", # BufferError
	"TTY": "+++ Invalid Processing Dimension +++ Please Change Current Universe And Reboot", # Platform doesn't support TTY
})