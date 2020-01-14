import os

def sort(d):
 s = list(d.keys())
 for i in range(len(s)):
  for j in range(i,len(s)):
   if d[s[j]] > d[s[i]]:
    c = s[j]
    s[j] = s[i]
    s[i] = c
 return s

adress = r"C:\Users\User\Desktop\Програмирование\Python\Геном\GRCh38.primary_assembly.genome.fa"
book = open(adress,'a')
book.write('E')
book.close()
k = int(input())
book = open(adress)
s=[]
s.append(' ')
for i in range(1,k):
	s.append(book.read(1))
f = dict({})
while s[k-1] != 'E':
	for i in range(k-1):
		s[i] = s[i+1]
	s[k-1]=book.read(1)
	if set(s).difference(('A','C','T','G')) != set():
		j = 0
		for j in range(k)[::-1]:
			if not(s[j] in ['A','C','T','G']):
				break
		for i in range(k-j):
			s[i] = s[j+i]
		for i in range(k-j+1,k):
			s[i] = book.read(1)
		continue
	st=''
	for i in range(k):
		st += s[i]
	if f.get(st,'#') == '#':
		f[st] = 1
	else:
		f[st] = f[st] + 1
	print(st,f[st])
print(f)
sn = []
sn = sort(f)
print(sn[0])
print(f.get(sn[0]))
print(sn[len(sn)-1])
print(f.get(sn[len(sn)-1]))
book.close()

