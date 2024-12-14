import sys,os,re,itertools

rawdata = [r.strip() for r in open('day_04.txt','rt').readlines()]
dir = {'NW':(-1,-1),'NE':(1,-1),'SW':(-1,1),'SE':(1,1)}

w,h = len(rawdata[0]),len(rawdata)

words = 0
[print(row) for row in rawdata]
for j in range(h):
  for i in range(w):
    print(i,j,rawdata[j][i])
    if rawdata[j][i] == 'A':
      print('found A',end=' ')
      cross = []
      for d in dir.keys():
        x,y = dir[d]
        nj = j+y
        ni = i+x
        if nj<0 or nj>=h or ni<0 or ni>=w:             
          print('!',end='')
        else:
          cross.append(rawdata[nj][ni])
          print('.',end='')
        if len(cross)==4: 
          match cross:
            case ['M','S','M','S']: words+=1
            case ['M','M','S','S']: words+=1
            case ['S','M','S','M']: words+=1
            case ['S','S','M','M']: words+=1

print(words)