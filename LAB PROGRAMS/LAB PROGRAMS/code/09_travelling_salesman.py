from itertools import permutations
d={'A':{'B':10,'C':15,'D':20},'B':{'A':10,'C':35,'D':25},'C':{'A':15,'B':35,'D':30},'D':{'A':20,'B':25,'C':30}}
best=min((['A']+list(p)+['A'] for p in permutations('BCD')), key=lambda p:sum(d[p[i]][p[i+1]] for i in range(4)))
print('Best tour:', ' -> '.join(best)); print('Cost:',sum(d[best[i]][best[i+1]] for i in range(4)))
