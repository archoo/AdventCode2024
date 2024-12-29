import sys,os,re,itertools,time
from utils import *

rawdata = [r.strip() for r in open('inputs/day_10.txt','rt').readlines()]
data = [list(row) for row in rawdata]
w,h = len(data[0]),len(data)

heads = []
for y in range(h):
  for x in range(w):
    if data[y][x]=='0': heads.append((x,y))
    data[y][x] = 0 if data[y][x] == '.' else int(data[y][x])
    
def display(delay=0):
  mv(1,1)
  for x in range(w):
    for y in range(h):
      put(str(data[y][x]),x,y,31)
  time.sleep(delay)

def oob(pt):
  return pt[0]<0 or pt[0]>=w or pt[1]<0 or pt[1]>=h

turtle()
display()

final1 = set()
final2 = set()

for head in heads:
  display()
  put(str(data[head[1]][head[0]]),head[0],head[1],97)
  trails=[[head]]
  step = 0
  while len(trails) > 0:
    t = trails.pop(0)
    hx,hy = t[-1]
    step = len(t)
    for d in ['N','E','S','W']:
      tx=hx+dir[d][0]
      ty=hy+dir[d][1]
      if not oob((tx,ty)) and data[ty][tx] == step:
        nt = t[:]
        nt.append((tx,ty))
        trails.append(nt)       
        if step == 9: 
          put(str(data[ty][tx]),tx,ty,33)
          final1.add((head,(tx,ty)))
          final2.add(str(nt))
        else: 
          put(str(data[ty][tx]),tx,ty,32)
      
print(f'\033[{h+2};{0}H',len(final1),len(final2))
