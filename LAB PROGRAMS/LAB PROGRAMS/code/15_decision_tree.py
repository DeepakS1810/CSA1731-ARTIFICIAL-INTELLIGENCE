# ID3 decision tree for categorical features.
from math import log2
data=[({'Outlook':'sunny','Wind':'weak'},'no'),({'Outlook':'sunny','Wind':'strong'},'no'),({'Outlook':'overcast','Wind':'weak'},'yes'),({'Outlook':'rain','Wind':'weak'},'yes'),({'Outlook':'rain','Wind':'strong'},'no')]
def entropy(rows):
 labels=[y for _,y in rows]; n=len(labels)
 return -sum((labels.count(y)/n)*log2(labels.count(y)/n) for y in set(labels))
def build(rows,attrs):
 labels=[y for _,y in rows]
 if len(set(labels))==1:return labels[0]
 if not attrs:return max(set(labels),key=labels.count)
 def gain(a):
  groups={v:[r for r in rows if r[0][a]==v] for v in {x[a] for x,_ in rows}}
  return entropy(rows)-sum(len(g)/len(rows)*entropy(g) for g in groups.values())
 a=max(attrs,key=gain); groups={v:[r for r in rows if r[0][a]==v] for v in {x[a] for x,_ in rows}}
 return (a,{v:build(g,[x for x in attrs if x!=a]) for v,g in groups.items()},max(set(labels),key=labels.count))
def predict(tree,x):
 if isinstance(tree,str):return tree
 a,branches,default=tree; return predict(branches[x[a]],x) if x[a] in branches else default
tree=build(data,['Outlook','Wind']); sample={'Outlook':'rain','Wind':'weak'}
print('Decision tree:',tree); print('Prediction for rain/weak:',predict(tree,sample))
