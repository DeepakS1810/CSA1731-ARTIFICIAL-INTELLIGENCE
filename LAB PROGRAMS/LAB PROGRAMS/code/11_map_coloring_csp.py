# Backtracking CSP: adjacent regions must have different colors.
g={'WA':['NT','SA'],'NT':['WA','SA','Q'],'SA':['WA','NT','Q','NSW','V'],'Q':['NT','SA','NSW'],'NSW':['Q','SA','V'],'V':['SA','NSW'],'T':[]}; colors=('red','green','blue'); assign={}
def solve():
 if len(assign)==len(g): return True
 v=next(x for x in g if x not in assign)
 for color in colors:
  if all(assign.get(n)!=color for n in g[v]):
   assign[v]=color
   if solve(): return True
   del assign[v]
 return False
solve()
print('Map coloring:'); [print(k,assign[k]) for k in g]
