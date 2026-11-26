from collections import deque
start=(1,2,3,4,0,6,7,5,8); goal=(1,2,3,4,5,6,7,8,0)
def neighbors(s):
 i=s.index(0); r,c=divmod(i,3)
 for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
  nr,nc=r+dr,c+dc
  if 0<=nr<3 and 0<=nc<3:
   j=nr*3+nc; t=list(s); t[i],t[j]=t[j],t[i]; yield tuple(t)
def solve():
 q=deque([start]); parent={start:None}
 while q:
  s=q.popleft()
  if s==goal: break
  for n in neighbors(s):
   if n not in parent: parent[n]=s; q.append(n)
 path=[]; s=goal
 while s is not None: path.append(s); s=parent[s]
 return path[::-1]
path=solve(); print('8-puzzle solved in',len(path)-1,'move(s)')
for s in path:
 for i in range(0,9,3): print(s[i:i+3])
 print()
