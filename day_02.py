import sys,os,re,itertools

rawdata = [[int(c) for c in r.strip().split()] for r in open('inputs/day_02.txt','rt').readlines()]
s=0
for row in rawdata:
  safe = True
  diff = []
  f = row[0]
  for i in range(1,len(row)):
    diff.append(row[i]-f)
    f = row[i]
  print(diff)
  diff.sort()
  print(diff)
  if diff[0]<0 and diff[-1]>0: 
    print('sign diff')
    safe = False
  adiff = [abs(d) for d in diff]
  if min(adiff)<1 or abs(max(adiff))>3: 
    print('too big')
    safe = False
  if safe: s+=1

print(s)  
