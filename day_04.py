import sys,os,re,itertools

rawdata = [r.strip() for r in open('inputs/day_04.txt','rt').readlines()]
dir = {'N':(0,-1),
       'NE':(1,-1),
       'E':(1,0),
       'SE':(1,1),
       'S':(0,1),
       'SW':(-1,1),
       'W':(-1,0),
       'NW':(-1,-1)}

w,h = len(rawdata[0]),len(rawdata)

words = []
[print(row) for row in rawdata]
for j in range(h):
  for i in range(w):
    print(i,j,rawdata[j][i])
    if rawdata[j][i] == 'X':
      print('found X',end=' ')
      for d in dir.keys():
        word = 'X'
        print('trying',d,end=' ')
        x,y = dir[d]
        for c in range(1,4):
          nj = j+(y*c)
          ni = i+(x*c)
          if nj<0 or nj>=h or ni<0 or ni>=w:             
            print('!',end='')
          else:
            n = rawdata[nj][ni]
            word += n
            print('.',end='')
        if len(word)==4: 
          words.append(word)
        print(word)
print(words.count('XMAS'))