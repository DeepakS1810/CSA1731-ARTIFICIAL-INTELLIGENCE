import heapq
graph={'A':{'B':1,'C':4},'B':{'C':2,'D':5},'C':{'D':1},'D':{}}; h={'A':3,'B':2,'C':1,'D':0}
q=[(h['A'],0,'A')]; came={'A':None}; cost={'A':0}
while q:
 f,g,u=heapq.heappop(q)
 if u=='D': break
 for v,w in graph[u].items():
  ng=g+w
  if ng<cost.get(v,float('inf')): cost[v]=ng; came[v]=u; heapq.heappush(q,(ng+h[v],ng,v))
path=[]; u='D'
while u is not None: path.append(u); u=came[u]
print('A* path:', ' -> '.join(path[::-1]), '| total cost:',cost['D'])
