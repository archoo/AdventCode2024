import sys,os,re,itertools

rawdata = [r.strip() for r in open('inputs/day_05.txt','rt').readlines() if r.strip() != '']
rules = []
updates = []
for row in rawdata:
  if '|' in row:
    rules.append(tuple([int(r) for r in row.split('|')]))
  else:
    updates.append([int(u) for u in row.split(',')])

rules.sort()

def swap(l: list,i1,i2):
  l1 = l.pop(i1)
  l.insert(i1,0)
  l2 = l.pop(i2)
  l.insert(i2,l1)
  l.pop(i1)
  l.insert(i1,l2)

v,u = 0,0
for upd in updates:
  valid = True
  stable = False
  while not stable:
    stable = True
    for r in rules:
      for i in range(len(upd)):
        if r[0] == upd[i]:
          f = upd.index(r[1]) if r[1] in upd else None
          if f != None and f < i:
            valid = False
            stable = False
            swap(upd,f,i)
  
  if valid: 
    v+=upd[(len(upd)//2)]
  else:
    u+=upd[(len(upd)//2)]
    
print('\n',v,u)
      
      