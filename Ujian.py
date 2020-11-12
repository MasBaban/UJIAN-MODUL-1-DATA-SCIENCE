# Soal Nomer 1
from random import randint

n = input('Input your phone number:')

def nomerhp(n):
    if n != range(0,9):
        print('Only positive number')
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

for mciNumbers in range(1):
	print('0912', nomerhp(3), "-", nomerhp(7))


# Soal Nomer 2
'''
def perpindahan(x):
  l=len(x)
  i=0
  while i<l:
    if x[i] is 0:
      x.append(x.pop(i))
      l=l-1
    else:
      i=i+1
  return x

print(perpindahan([False,1,0,1,2,0,1,3,"a"]))
print(perpindahan([0,2,8,9,0,True,False,"1",8]))
print(perpindahan([0,True,True,False,'a','b',1,1,1]))
'''
# Soal Nomer 3
'''
class statistik:
    def __init__(self,first,last,std):
        self.mean = st.mean
        self.median = st.median
        self.mode = st.mode
        self.std  = st.std
'''
        