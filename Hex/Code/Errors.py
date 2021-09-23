from threading_print import print

class errors():
	def __init__(self, d: dict, lines) -> dict:
		"""
		Generates a dict of Python exceptions classes given a dict of the format {"ErrorName": "ErrorMessage"} 
		"""

		self.e = {}
		self.lines = lines

		def Err_Init(self, func=exit, end="\n"):
			print("\u001b[31m%s" % self.msg, flush=True, end=end)
			func()
		
		for k, v in d.items():
			self.e[k] = type(k, (Exception,), {"__init__": Err_Init, "msg": v})
		
	def __call__(self, err: str, lineno, end="\n"):
		print("\u001b[31mError on line %s: %s" % (lineno, self.lines[lineno]), end=end)
		self.e[err](end)