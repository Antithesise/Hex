from time import time, sleep as wait

# Typing
from typing import NamedTuple

# Hex imports
from threading_print import print

# System checks
from Checks import check
check()

# Definitions
def sleep(secs: float) -> None:
	"""
	sleep(seconds)
	Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision.
	"""

	wait(secs)

struct_time_type_fields = {
	"tm_year": "year, for example, 1993",
	"tm_mon": "month of year, range [1, 12]",
	"tm_mday": "day of month, range [1, 31]",
	"tm_hour": "hours, range [0, 23]",
	"tm_min": "minutes, range [0, 59]",
	"tm_sec": "seconds, range [0, 61])",
	"tm_wday": "day of week, range [0, 6], Monday is 0",
	"tm_yday": "day of year, range [1, 366]",
	"tm_isdst": "1 if daylight saving time is in effect, 0 if not, and -1 if unknown",
	"tm_zone": "abbreviation of timezone name",
	"tm_gmtoff": "offset from UTC in seconds",
}

YN = {
	2007: "Reversed Ptarmigan",
	2008: "Three Roses",
	2009: "Pensive Hare",
	2010: "Happy Goose",
	2011: "Complicated Monkey",
	2012: "Second Inception",
	2013: "Frog Ascendant",
	2014: "Reciprocating Llama",
	2015: "Spinning Mouse",
	2016: "Sneezing Panda",
	2017: "Backwards-Facing Artichoke",
	2018: "Justifiably Defensive Lobster",
	2019: "Incontrovertible Skunk",
	2020: "Condescending Carp",
	2021: "Beleaguered Badger",
}

class struct_time(NamedTuple):
	tm_year: int
	tm_mon: int
	tm_mday: int
	tm_hour: int
	tm_sec: int
	tm_wday: int
	tm_yday: int
	tm_isdst: int
	tm_zone: str
	tm_gmtoff: int

def localtime():
	pass

def asctime(t=None):
	T = t if t != None else localtime()

def htime(secs=None):
	S = secs if secs else time()


# Runtime
if __name__ == "__main__":
	print(struct_time(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))