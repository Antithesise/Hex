from UnrealTimeClock import UnrealTimeClock
from os.path import dirname, isfile, realpath
from sys import argv, platform
from Aquarium import Aquarium
from Htime import time, sleep
from threading import Thread
from Errors import errors
from os import system

from threading_print import print

class Beehive():
	def __init__(self, beehive):
		self.path = beehive
		with open(beehive, "r") as hive:
			self.beedict = {iolines[-1].split(" = ")[0]:iolines[-1].split(" = ")[1] for iolines[-1] in hive.readlines()}
		self.updatehive()
	
	def updatehive(self):
		with open(self.path, "w") as hive:
			hive.write("\n".join([k + " = " + v for k, v in self.beedict.items()]))

	def set(self, key, value):
		self.beedict[key] = value
		self.updatehive()

	def get(self, key):
		return self.beedict[key]

global iolines, start, variable, beehive, lines, lineindex, maxlines, e
iolines = []
start = time()
variables = {}
beehive = Beehive(dirname(realpath(__file__)) + "/.beehive")
lines = []
lineindex = 0
maxlines = 18
e = errors({
	"!": "+++!!!!!+++", # Exception
	"?": "+++?????+++", # Warning
	"Address": "+++ Error At Address: 14, Treacle Mine Road, Ankh-Morpork +++ Please Reinstall Universe And Reboot", # LookupError/KeyError
	"Cheese": "+++ Out Of Cheese Error +++ Redo From Start", # TimeoutError/MemoryError
	"Soon":"+++ Cominge Soon To A Pt Nr. You +++ Request Banged Grains And Install When Ready", # NotImplementedError
	"Cucumber": "+++ Divide By Cucumber Error +++ Please Reinstall Universe And Reboot", # ZeroDivisionError
	"Data": "+++ Insufficient Data +++ Redo From Start", # TypeError
	"Domain": "+++ Eternal Domain Error +++ Redo From Start", # OSError
	"Jelly": "+++ Mr. Jelly! Mr. Jelly! +++ Redo From Start", # SystemError
	"Melon": "+++ MELON MELON MELON +++ Redo From Start", # ValueError/NameError
	"Mine": "\nMine! Waah!", # FileNotFoundError
	"Mum": "+++ Hi Mum Is Testing +++ Redo From Start", # SyntaxError
	"One": "+++ Oneoneoneoneoneone +++ Redo From Start", # ArithmeticError
	"Shrimp": "+++ Millenium Hand And Shrimp +++ Thinking Interrupted", # KeyboardInterrupt
	"Temp": "+++ Empty Temp Error +++ Redo From Start", # ReferenceError
	"Whoops": "+++ Whoops! Here Comes the Cheese! +++ Redo From Start", # BufferError
})

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

	return compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]").sub('', string)
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
	global main
	while func():
		sleep(1)
		if round(time()) % 840 == 0: # parps every 14 minutes
			pass # play parp sound

def Main():
	global iolines, start, variables, beehive, e

	clear()

	verbose = "-v" in argv

	temp = ""
	tempclearindex = 0
	start = time()

	try:
		no = 0
		while True:
			newioline = ""
			while not (newioline := input("").split("# ")[0].strip()):
				pass
			iolines += [newioline]
			
			tempclearindex -= 1
			
			if verbose:
				addline("\u001b[38;5;118m" + iolines[-1] + ": \u001b[0m")
				printtext()

			if "previous" in iolines[-1]:
				if tempclearindex >= 0: 
					iolines[-1] = iolines[-1].replace("previous", temp)
				else:
					e["Temp"]()

			if iolines[-1][:3] == "GBL":
				cmdmsg = 0
				if no:
					e["Mum"]()
			if not no:
				e["Mum"]()
			elif iolines[-1][:3] == "BRL":
				cmdmsg = 1
			elif iolines[-1][:16] == "mouse add cheese":
				cmdmsg = 2
				start = time()
			elif " beehive " in iolines[-1]:
				cmdmsg = 3
				try:
					if "" in [iolines[-1].split()[0].strip(), iolines[-1][len(iolines[-1].split()[0]) + 9:]]:
						e["Data"]()
				except IndexError:
					e["Data"]()
				beehive.set(iolines[-1].split()[0], iolines[-1][len(iolines[-1].split()[0]) + 9:])
			elif "beehive " in iolines[-1]:
				cmdmsg = 4
				try:
					if "" in [iolines[-1].split()[1].strip()]:
						e["Data"]()
				except IndexError:
					e["Data"]()
				temp = beehive.get(iolines[-1].split()[1])
				tempclearindex = 2
			elif " set " in iolines[-1]:
				cmdmsg = 5
				try:
					if "" in [iolines[-1].split()[0], iolines[-1][len(iolines[-1].split()[0]) + 5:]]:
						e["Data"]()
				except IndexError:
					e["Data"]()
				variables[iolines[-1].split()[0]] = iolines[-1][len(iolines[-1].split()[0]) + 5:]
			elif len(iolines[-1][:-2].split()) == 1 and iolines[-1].rstrip().split("\n")[0] in variables.keys():
				cmdmsg = 4
				temp = variables[iolines[-1][:].split()[0]]
				tempclearindex = 2
			elif iolines[-1][:5] == "wait ":
				cmdmsg = 6
				try:
					if "" in [iolines[-1][5:]]:
						e["Data"]()
					float(iolines[-1][5:])
				except IndexError:
					e["Data"]()
				except ValueError:
					e["Melon"]()
				sleep(float(iolines[-1][5:]))
			elif iolines[-1][:4] == "say ":
				cmdmsg = 7
			elif iolines[-1][:4] == "Why?":
				cmdmsg = 8
			elif iolines[-1][:13] == "Why anything?":
				cmdmsg = 9
			elif " add " in iolines[-1]:
				cmdmsg = 10
				try:
					variables[iolines[-1].split(" add ")[0]] = int(variables[iolines[-1].split(" add ")[0]]) + int(iolines[-1].split(" add ")[1])
				except ValueError:
					variables[iolines[-1].split(" add ")[0]] += iolines[-1].split(" add ")[1]
				except KeyError:
					e["Melon"]()
			else:
				cmdmsg = 4
				temp = iolines[-1]
				tempclearindex = 2

			if verbose or cmdmsg in [7]:
				addline([
					"Program Initiated.",
					"Terminating Session.",
					"time until more cheese needed: 10s.",
					"%s:'%s' addded to beehives." % (iolines[-1].split()[0], iolines[-1][len(iolines[-1].split()[0]) + 9:]),
					"'%s' moved to temp storage." % temp,
					"%s = '%s'" % (iolines[-1].split()[0], iolines[-1][len(iolines[-1].split()[0]) + 5:]),
					"T = %s. Done!" % iolines[-1][5:],
					iolines[-1][4:],
					"Because",
					"Because everything",
					"%s added to %s" % (iolines[-1].split(" add ")[0], iolines[-1].split(" add ")[1]),
				][cmdmsg], False)
				printtext()

			if cmdmsg == 1:
				sleep(0.5)
				exit()
			if cmdmsg == 9:
				e["Domain"]()
	except MemoryError:
		e["Cheese"]()
	except KeyboardInterrupt:
		e["Shrimp"]()

main = Thread(target=Main, args=[])
main.start()

Thread(target=UnrealTimeClock, args=[main.is_alive]).start()
Thread(target=aquarium, args=[main.is_alive]).start()
Thread(target=Parp, args=[main.is_alive]).start()

while main.is_alive():
	if time() - start > 10:
		e["Cheese"]()
	if isfile("./.FTB"):
		e["Mine"]()