from os.path import dirname, isfile, realpath
from sys import argv, platform
from threading import Thread
from os import system

# Typing
from Typing import 

# System checks

from Checks import check
check(errs=e, args=argv)

# Hex Imports

from UnrealTimeClock import UnrealTimeClock
from threading_print import print
from Aquarium import Aquarium
from Htime import time, sleep
from Errors import errors

# Variables

global start, variable, beehive, lines, lineindex, maxlines, e

with open(argv[1], "r") as iohexfile:
	rawhexfile = [line for line in iohexfile.readlines()]

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
}, rawhexfile)

start = time()
variables = {}
lines = []
lineindex = 0
maxlines = 18

# Classes

class Beehive():
	def __init__(self, beehive):
		self.path = beehive
		try:
			with open(beehive, "r") as hive:
				self.beedict = {line.split(" = ")[0]:line.split(" = ")[1] for line in hive.readlines()}
		except FileNotFoundError:
			pass
		self.updatehive()
	
	def updatehive(self):
		with open(self.path, "w") as hive:
			hive.write("\n".join([k + " = " + v for k, v in self.beedict.items()]))

	def set(self, key, value):
		self.beedict[key] = value
		self.updatehive()

	def get(self, key):
		return self.beedict[key]

# Functions

def addline(line, newline=True):
	global lines

	if newline or lines == []:
		lines += [line]
	else:
		lines[-1] += line

def getlines():
	global lines, lineindex, maxlines

	return [lines[i - lineindex] for i in range(-min(len(lines), maxlines), 0)] if len(lines) else []

def getline(line):
	global lines, lineindex, maxlines

	return [lines[i - lineindex] for i in range(-min(len(lines), maxlines), 0)][min(maxlines - 1, line)] if len(lines) else ""

# \/ https://www.tutorialspoint.com/How-can-I-remove-the-ANSI-escape-sequences-from-a-string-in-python \/
def delansi(string):
	from re import compile

	return compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]").sub("", string)
# /\ https://www.tutorialspoint.com/How-can-I-remove-the-ANSI-escape-sequences-from-a-string-in-python /\

def aquarium(func):
	global lines, maxlines

	a = Aquarium(0, 0)
	while func():
		a(len(delansi(getline(-1))), min(len(lines) - bool(len(lines)), maxlines)) # move cursor y lines beneath frame and x across
		sleep(0.2)
	print()

def catch(): # pass as an argument when calling error to prevent sys.exit()
	pass

def clear():
	system("cls" if platform == "win32" else "clear")

def printtext():
	clear()
	print(end="\r\u001b[1000A\u001b[31B" + "\n".join(getlines()), flush=True)

def Parp(func):
	from replit import audio

	global main
	while func():
		sleep(1)
		if round(time()) % 840 == 0: # parps every 14 minutes
			audio.play_file("parp.wav")

def Main(rawhexfile):
	global start, variables, beehive, e

	clear()

	hexfile = [line.split("# ")[0].strip() for line in rawhexfile]
				
	if hexfile[0].split("# ")[0].rstrip() != "GBL":
		e("Mum", 0)

	verbose = "-v" in argv

	temp = ""
	tempclearindex = 0
	start = time()

	for no, line in enumerate(hexfile):
		try:
			if not line.split("# ")[0].strip():
				continue

			tempclearindex -= 1
			
			if verbose:
				addline("\u001b[38;5;118m" + line + ": \u001b[0m")
				printtext()

			if "previous" in line:
				if tempclearindex >= 0: 
					line = line.replace("previous", temp)
				else:
					e("Temp", no)

			if line[:3] == "GBL":
				cmdnum = 0
				if no:
					e("Mum", no)
			elif line[:3] == "BRL":
				cmdnum = 1
			elif line[:16] == "mouse add cheese":
				cmdnum = 2
				start = time()
			elif " beehive " in line:
				cmdnum = 3
				try:
					if "" == line.split(" beehive ", 1)[0].strip() or "" == line.split(" beehive ", 1)[1].strip():
						e("Data", no)
				except IndexError:
					e("Data", no)
				beehive.set(line.split(" beehive ", 1)[0].strip(), line.split(" beehive ", 1)[1].strip())
			elif "beehive " in line:
				cmdnum = 4
				try:
					if "" == line.split("beehive ", 1)[1].strip():
						e("Data", no)
				except IndexError:
					e("Data", no)
				temp = beehive.get(line.split("beehive ", 1)[1].strip())
				if temp == None:
					e("Address", no)
				tempclearindex = 2
			elif " set " in line:
				cmdnum = 5
				try:
					if "" in [line.split(" set ", 1)[0].strip(), line.split(" set ", 1)[1].strip()]:
						e("Data", no)
				except IndexError:
					e("Data", no)
				variables[line.split(" set ", 1)[0].strip()] = line.split(" set ", 1)[1].strip()
			elif line.strip() in variables.keys():
				cmdnum = 4
				temp = variables[line.strip()]
				tempclearindex = 2
			elif "wait " in line:
				cmdnum = 6
				try:
					if "" == line.split("wait ", 1)[1].strip():
						e("Data", no)
					sleep(float(line.split("wait ", 1)[1].strip()))
				except IndexError:
					e("Data", no)
				except ValueError:
					e("Melon", no)
			elif "say " in line:
				cmdnum = 7
			elif "Why" == line:
				cmdnum = 8
			elif "Why anything?" == line:
				cmdnum = 9
			elif " add " in line:
				cmdnum = 10
				try:
					variables[line.split(" add ", 1)[0]] = float(variables[line.split(" add ", 1)[0]]) + float(line.split(" add ", 1)[1])
				except ValueError:
					variables[line.split(" add ", 1)[0]] += line.split(" add ", 1)[1]
				except KeyError:
					e("Address", no)
			else:
				cmdnum = 4
				temp = line
				tempclearindex = 2

			if verbose or cmdnum in [7]:
				addline([
					"Program Initiated.",
					"Terminating Session.",
					"time until more cheese needed: 10s.",
					"%s:'%s' addded to beehives." % (line.split()[0], line[len(line.split()[0]) + 9:]),
					"'%s' moved to temp storage." % temp,
					"%s = '%s'" % (line.split()[0], line[len(line.split()[0]) + 5:]),
					"T = %s. Done!" % line.split("wait ", 1)[1].strip(),
					"%s" % line.split("say ", 1)[1].strip(),
					"Because",
					"Because everything. ",
					"%s added to %s" % (line.split(" add ", 1)[0], line.split(" add ", 1)[1]),
				][cmdnum], False)
				printtext()

			if cmdnum == 1:
				sleep(0.5)
				exit()
			if cmdnum == 9:
				e("Domain", no, end="")
		except MemoryError:
			e("Cheese", no)
		except KeyboardInterrupt:
			e("Shrimp", no)
		except Exception as e:
			print("\u001b[31mError on line %s: %s" % (no, rawhexfile[no]))
			raise e

# runtime

if __name__ != "__main__":
	beehive = Beehive(dirname(realpath(__file__)) + "/.beehive")

	main = Thread(target=Main, args=[rawhexfile], daemon=True)
	main.start()

	Thread(target=UnrealTimeClock, args=[main.is_alive]).start()
	Thread(target=aquarium, args=[main.is_alive]).start()
	Thread(target=Parp, args=[main.is_alive]).start()

	while main.is_alive():
		if time() - start > 10:
			e["Cheese"]()
		if isfile("./.FTB"):
			e["Mine"]()