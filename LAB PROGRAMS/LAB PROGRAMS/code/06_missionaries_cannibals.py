from collections import deque
# State: missionaries left, cannibals left, boat side (0=left,1=right).
start=(3,3,0); goal=(0,0,1); moves=((1,0),(2,0),(0,1),(0,2),(1,1))
def safe(m,c): return 0<=m<=3 and 0<=c<=3 and (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)
q=deque([start]); prev={start:None}
while q:
 s=q.popleft()
 if s==goal: break
 m,c,b=s
 for x,y in moves:
  t=(m-x,c-y,1) if b==0 else (m+x,c+y,0)
  if safe(t[0],t[1]) and t not in prev: prev[t]=s; q.append(t)
path=[]; s=goal
while s is not None: path.append(s); s=prev[s]
print('M C boat (L-bank counts; 0=L, 1=R):')
for s in reversed(path): print(s)
