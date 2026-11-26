from collections import deque
# Jugs hold 4L and 3L; reach exactly 2L in the 4L jug.
start=(0,0); q=deque([start]); parent={start:None}
while q:
 a,b=q.popleft()
 if a==2: goal=(a,b); break
 moves={(4,b),(a,3),(0,b),(a,0),(a-min(a,3-b),b+min(a,3-b)),(a+min(b,4-a),b-min(b,4-a))}
 for s in moves:
  if s not in parent: parent[s]=(a,b); q.append(s)
path=[]; s=goal
while s is not None: path.append(s); s=parent[s]
print('States (4L jug, 3L jug):', list(reversed(path)))
