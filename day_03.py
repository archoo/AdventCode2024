import sys,os,re,itertools

rawdata = [r for r in open('inputs/day_03.txt','rt').readlines()]
t=0
go = True
for row in rawdata:
  mul = re.finditer(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))",row)
  for m in mul:
    print(m.group(0),end=' ')
    match m.group(0):
      case "do()": go = True
      case "don't()": go = False
      case _: 
        if go: 
          a,b = m.group(0)[4:-1].split(',')
          t += int(a)*int(b)
          print(t)
        else:
          print('-')
print(t)
