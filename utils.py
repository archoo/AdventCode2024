def swap(l: list,i1,i2):
  l1 = l.pop(i1)
  l.insert(i1,0)
  l2 = l.pop(i2)
  l.insert(i2,l1)
  l.pop(i1)
  l.insert(i1,l2)

dir = {'N':(0,-1),
       'NE':(1,-1),
       'E':(1,0),
       'SE':(1,1),
       'S':(0,1),
       'SW':(-1,1),
       'W':(-1,0),
       'NW':(-1,-1)}

def mv(x,y):
  print(f'\033[{y};{x}H',end='')

def put(ch,x,y,col=0):
  print(f'\033[{y};{x}H',end='')
  print(f'\033[{col}m'+ch+'\033[0m',end='')
  print(end='',flush=True)
  
def int2base(num, base, abc="0123456789abcdefghijklmnopqrstuvwxyz"):
  if num < 0:
    return '-' + int2base(-num, base, abc)
  output = abc[num % base] # rightmost digit
  while num >= base:
    num //= base # move to next digit to the left
    output = abc[num % base] + output # this digit
  return output