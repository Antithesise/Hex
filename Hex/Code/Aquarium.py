from random import choice, randint
from functools import lru_cache

# Typing
from typing import Union

# System checks
from Checks import check
check()

# Hex imports
from threading_print import print
from Htime import sleep


# Definitions
class fish:
	def __init__(self, bg):
		self.x = randint(0, 119)
		self.y = randint(0, 26)
		self.z = (randint(0, 1) * 2) - 1
		self.vel = [randint(0 - self.x, 119 - self.x), randint((-self.y if self.y < 2 else -2), (self.y - 27 if self.y > 27 else 2))]
		self.i = abs(self.vel[0])
		self.colour = "\u001b[38;5;%sm" % choice([27, 27, 208, 208, 234, 234, 252, 252])
		self.bg = bg

	def update(self):
		from random import randint
		if self.i <= 1:
			self.vel = [randint(0 - self.x, 119 - self.x), randint((-self.y if self.y < 2 else -2), (self.y - 27 if self.y > 27 else 2))]
			self.i = abs(self.vel[0] - 1)
			if self.bg[self.y][self.x] == "\u001b[48;5;45m":
				self.z = -self.z
		self.i -= 1
		if self.vel[0]:
			self.x += int(self.vel[0]/abs(self.vel[0]))
		if self.vel[1] and self.vel[0]:
			if round(abs(self.vel[0]) / abs(self.vel[1])):
				if not self.i % round(abs(self.vel[0]) / abs(self.vel[1])):
					self.y += int(self.vel[1]/abs(self.vel[1]))

	def __call__(self):
		if self.bg[self.y][self.x] == "\u001b[48;5;45m" or self.z == 1:
			if abs(self.vel[0]):
				return "\r\u001b[1000A\u001b[%dC\u001b[%dB" % (self.x, self.y) + self.bg[self.y][self.x] + self.colour + ("}<#>" if self.vel[0]/abs(self.vel[0]) == 1 else "<#>{")
			else:
				return "\r\u001b[1000A\u001b[%dC\u001b[%dB" % (self.x, self.y) + self.bg[self.y][self.x] + self.colour + "}<#>"
		else:
			return ""

class Aquarium:
	@lru_cache(maxsize=120)
	def __init__(self, x, y):
		from random import choice, shuffle, randint
		
		def __shuffled(x, t):
			for s in range(t):
				shuffle(x)
			return x

		self.bg = [
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;5;45m"] * 120,
			["\u001b[48;2;142;86;46m" for i in range(3)] + ["\u001b[48;5;45m" for i in range(117)],
			["\u001b[48;2;142;86;46m" for i in range(8)] + ["\u001b[48;5;45m" for i in range(112)],
			["\u001b[48;2;142;86;46m" for i in range(11)] + ["\u001b[48;5;45m" for i in range(109)],
			["\u001b[48;2;142;86;46m" for i in range(13)] + ["\u001b[48;5;45m" for i in range(107)],
			["\u001b[48;2;142;86;46m" for i in range(14)] + ["\u001b[48;5;45m" for i in range(106)],
			["\u001b[48;2;142;86;46m" for i in range(15)] + ["\u001b[48;5;45m" for i in range(105)],
			["\u001b[48;2;142;86;46m" for i in range(15)] + ["\u001b[48;5;45m" for i in range(105)],
			["\u001b[48;2;142;86;46m" for i in range(16)] + ["\u001b[48;5;45m" for i in range(104)],
			["\u001b[48;2;142;86;46m" for i in range(16)] + ["\u001b[48;5;45m" for i in range(104)],
			["\u001b[48;2;142;86;46m" for i in range(16)] + ["\u001b[48;5;45m" for i in range(104)],
			["\u001b[48;2;142;86;46m" for i in range(17)] + ["\u001b[48;5;45m" for i in range(103)],
			["\u001b[48;2;142;86;46m" for i in range(17)] + ["\u001b[48;5;45m" for i in range(103)],
			["\u001b[48;2;142;86;46m" for i in range(17)] + ["\u001b[48;5;45m" for i in range(103)],
		] + [
			[
				"\u001b[38;5;%dm\u001b[48;5;%dm" % (
					choice([137, 143, 143, 144, 144, 180, 180, 180, 228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 243]), choice([137, 143, 143, 144, 144, 180, 180, 180, 228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 228, 243])
				) for i in range(120)
			] for j in range(3)
		]
		self.bglines = "\n".join([" ".join(row) for row in self.bg])

		self.fishes = [fish(self.bg) for f in range(randint(2, 17))]
		self.x = x
		self.y = y

	def __call__(self, endx=0, endy=0):
		for f in self.fishes:
			f.update()
		print(
			end="\r\u001b[1000A" +
			self.bglines +
			"".join([f() for f in self.fishes]) +
			"\r\u001b[1000A\u001b[%dC\u001b[%dB" % (endx, 31 + endy) +
			("" if endx else "\r"),
			flush=True
		)


# Runtime
if __name__ == "__main__":
	a = Aquarium(0, 0)

	while True:
		a()
		sleep(0.2)
