import sys,os,re,itertools
from utils import *

rawdata = [[r.strip().split(':')[0],r.strip().split(':')[1].strip().split()] for r in open('inputs/day_07.txt','rt').readlines()]
newdata = []
tot = 0
tot_oper = 3
for row in rawdata:
  print()
  valid = False
  tgt = int(row[0])
  print(tgt)
  nums = [int(c) for c in row[1]]
  opt = len(nums)-1
  for o in range(pow(tot_oper,opt)):
    res = ''
    oper = str(int2base(o,tot_oper)).rjust(opt,'0')
    n = nums[0]
    res += str(n)
    for i in range(len(nums)-1):
      m = nums[i+1]
      match oper[i]:
        case '2':
          n = int(str(n)+str(m))
          res+='|'
        case '1': 
          n = n+m
          res+='+'
        case '0': 
          n = n*m
          res+='*'
      res+=str(m)
    res+=f'={n}'
    if tgt==n: 
      valid=True
      print('  ',res)
  if valid: 
    tot += tgt

print(tot)
      
    
    