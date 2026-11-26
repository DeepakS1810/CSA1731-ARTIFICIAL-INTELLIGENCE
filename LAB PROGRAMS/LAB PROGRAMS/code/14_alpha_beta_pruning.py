tree={'A':['B','C'],'B':['D','E'],'C':['F','G']}; values={'D':3,'E':5,'F':2,'G':9}; pruned=[]
def ab(n,alpha,beta,max_turn):
 if n in values:return values[n]
 if max_turn:
  v=-float('inf')
  for c in tree[n]:
   v=max(v,ab(c,alpha,beta,False)); alpha=max(alpha,v)
   if alpha>=beta: pruned.extend(tree[n][tree[n].index(c)+1:]); break
  return v
 v=float('inf')
 for c in tree[n]:
  v=min(v,ab(c,alpha,beta,True)); beta=min(beta,v)
  if beta<=alpha: pruned.extend(tree[n][tree[n].index(c)+1:]); break
 return v
print('Alpha-beta value:',ab('A',-float('inf'),float('inf'),True)); print('Pruned branches:',pruned)
