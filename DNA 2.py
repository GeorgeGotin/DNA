def file_reader(f):
	t = book.read()
	return t

def stronl(t,s,els=''):
	res = ''
	for i in t:
		if i in s:
			res+=i
		else:
			res+=els
	return res

def sort(d):
 s = list(d.keys())
 for i in range(len(s)):
  for j in range(i,len(s)):
   if d[s[j]] > d[s[i]]:
    c = s[j]
    s[j] = s[i]
    s[i] = c
 return s

k = int(input())
book = open(r"C:\Users\User\Desktop\Програмирование\Python\Геном\GRCh38.primary_assembly.genome.fa")
print('book is opened')
t = file_reader(book)
book.close()
print('t is writed')
text = stronl(t,('A','C','T','G'),els=' ')
print(text)
f = dict({})
for i in range(len(text) - k):
	w=''
	for j in range(k):
		w = w + text[i+j]
	if ' ' in w:
		continue
	if f.get(w,'#') == '#':
		f[w] = 1
	else:
		f[w] = f[w] + 1
print(f)
s = sort(f)
print(s[0],f[s[0]],'\n',s[len(s)-1],f[s[len(s)-1]])

