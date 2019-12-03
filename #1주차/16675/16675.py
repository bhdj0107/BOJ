import sys
import copy

temp = sys.stdin.readline()
M = set(temp.split()[0:2])
T = set(temp.split()[2:4])
win = {'R':'P', 'P':'S', 'S':'R'}

if len(M) == 1 and win[copy.deepcopy(M).pop()] in T:
	print("TK")
	exit()
if len(T) == 1 and win[copy.deepcopy(T).pop()] in M:
	print("MS")
	exit()


print("?")