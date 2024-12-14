import sys,os,re,itertools

rawdata = [[int(c) for c in r.strip().split()] for r in open('day_02.txt','rt').readlines()]
s=0
def check(row):
  safe = True
  diff = []
  f = row[0]
  for i in range(1,len(row)):
    diff.append(row[i]-f)
    f = row[i]
  diff.sort()
  if diff[0]<0 and diff[-1]>0: 
    print('sign diff')
    safe = False
  adiff = [abs(d) for d in diff]
  if min(adiff)<1 or abs(max(adiff))>3: 
    print('too big')
    safe = False
  return safe

for nrow in rawdata:
  print()
  safe = check(nrow)
  print(nrow,safe)
  for x in range(len(nrow)):
    row = nrow[:]
    row.pop(x)
    safe = safe or check(row)
    print(row,safe)
  if safe: s+=1

print(s)  
