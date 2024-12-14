import sys,os,re,itertools

rawdata = [r.strip() for r in open('day_01.txt','rt').readlines()]
l1,l2 = [],[]
for row in rawdata:
  a,b = row.split()
  l1.append(int(a))
  l2.append(int(b))
l1.sort()
l2.sort()
t = 0
for i in range(len(l1)):
  t += abs(l1[i]-l2[i])
print(l1,l2)
print(t)

t = 0
for i in l1:
  t += i*l2.count(i)
print(t)