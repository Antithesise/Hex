from time import time 

# Typing

from typing import NamedTuple

# Hex imports

from threading_print import print

def sleep(secs: float) -> None:
	"""
	sleep(seconds)
	Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision.
	"""

	from time import sleep as wait

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

class struct_time:
	def __new__(self, tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst, tm_zone, tm_gmtoff):
		self = NamedTuple("struct_time", ["tm_year", "tm_mon", "tm_mday", "tm_hour", "tm_sec", "tm_wday", "tm_yday", "tm_isdst"])(tm_year=tm_year, tm_mon=tm_mon, tm_mday=tm_mday, tm_hour=tm_hour, tm_sec=tm_sec, tm_wday=tm_wday, tm_yday=tm_wday, tm_isdst=tm_isdst).__class__
		return NamedTuple("struct_time", ["tm_year", "tm_mon", "tm_mday", "tm_hour", "tm_sec", "tm_wday", "tm_yday", "tm_isdst"])(tm_year=tm_year, tm_mon=tm_mon, tm_mday=tm_mday, tm_hour=tm_hour, tm_sec=tm_sec, tm_wday=tm_wday, tm_yday=tm_wday, tm_isdst=tm_isdst)

def localtime():
	pass

def asctime(t=None):
	T = t if t != None else localtime()

def htime(secs=None):
	S = secs if secs else time()

if __name__ == "__main__":
	print(struct_time(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))