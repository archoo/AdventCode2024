import sys,os,re,itertools,copy,time
from utils import *

rawdata = [r.strip() for r in open('inputs/day_08_test.txt','rt').readlines()]
data = [list(r) for r in rawdata]
w,h = len(data[0]),len(data)
nodes = copy.deepcopy(data)
perim = [[x,0] for x in range(w)]
perim += [[w-1,y] for y in range(h)]
perim += [[w-x-1,h-1] for x in range(w)]
perim += [[0,h-y-1] for y in range(h)]

print(f'\033[?25l')
  
def display():
  os.system('color & cls')
  for x in range(w):
    for y in range(h):
      c = data[y][x]
      match(c):
        case '.': put(c,x,y,37)
        case _: put(c,x,y,33)

display()
paths = {}

for x in range(w):
  for y in range(h):
    # display()
    for p in perim:
      ant = {}
      line = plotLine(x,y,p[0],p[1])
      if line:
        i = 0
        for l in line:
          c=data[l[1]][l[0]]
          if c != '.': 
            ant.setdefault(c,[])
            ant[c].append(i)
          i+=1
      
      poss = {a:ant[a] for a in ant.keys() if len(ant[a])==2}
      if len(poss.keys())>0:
        paths[(x,y)] = poss

nodes = 0
for x,y in paths:
  for ant in paths[(x,y)]:
    if paths[(x,y)][ant][1]==paths[(x,y)][ant][0]*2:
      put('#',x,y,33)
      nodes+=1

print(f'\033[{h+2};{0}H',nodes)  