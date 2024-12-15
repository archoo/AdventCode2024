import sys,os,re,itertools
from utils import *

rawdata = [r.strip() for r in open('inputs/day_08.txt','rt').readlines()]
data = [list(r) for r in rawdata]
w,h = len(data[0]),len(data)
ants = {}
for x in range(w):
  for y in range(h):
    c = data[y][x]
    if c != '.':
      ants.setdefault(c,[])
      ants[c].append((x,y))

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

def oob(x,y):
  return x<0 or x>=w or y<0 or y>=h

nodes1 = set()
nodes2 = set()
for a in ants:
  for p in itertools.permutations(ants[a],2):
    a1,a2 = p
    dx = a2[0]-a1[0]
    dy = a2[1]-a1[1]
    a3 = (a2[0]+dx,a2[1]+dy) 
    a4 = (a1[0]-dx,a1[1]-dy)
    if not oob(a3[0],a3[1]): nodes1.add(a3)
    if not oob(a4[0],a4[1]): nodes1.add(a4)
    n = (a2[0]-dx,a2[1]-dy)
    while not oob(n[0],n[1]):
      nodes2.add(n)
      n = (n[0]-dx,n[1]-dy)

    n = (a1[0]+dx,a1[1]+dy)
    while not oob(n[0],n[1]):
      nodes2.add(n)
      n = (n[0]+dx,n[1]+dy)


for n in nodes2: put('#',n[0],n[1],33)
for n in nodes1: put('#',n[0],n[1],35)

print(f'\033[{h+2};{0}H',len(nodes1),len(nodes2))

