# Minimax on a small game tree (leaf utilities from MAX perspective).
tree={'A':['B','C'],'B':['D','E'],'C':['F','G']}; values={'D':3,'E':5,'F':2,'G':9}
def minimax(n,max_turn):
 if n in values:return values[n]
 scores=[minimax(c,not max_turn) for c in tree[n]]
 return max(scores) if max_turn else min(scores)
print('Best minimax value for MAX:',minimax('A',True))
