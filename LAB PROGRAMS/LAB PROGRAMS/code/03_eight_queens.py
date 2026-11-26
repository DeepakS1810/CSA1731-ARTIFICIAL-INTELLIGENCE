N=8; cols=set(); d1=set(); d2=set(); place=[]
def search(r=0):
 if r==N: return True
 for c in range(N):
  if c not in cols and r-c not in d1 and r+c not in d2:
   cols.add(c); d1.add(r-c); d2.add(r+c); place.append(c)
   if search(r+1): return True
   place.pop(); cols.remove(c); d1.remove(r-c); d2.remove(r+c)
 return False
search()
print('One 8-queens solution (Q = queen):')
for c in place: print(' '.join('Q' if j==c else '.' for j in range(N)))
