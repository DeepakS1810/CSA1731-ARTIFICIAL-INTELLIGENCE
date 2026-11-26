# Maximize f(x)=x^2 for integer x in [0,31].
import random
random.seed(7); pop=[random.randrange(32) for _ in range(12)]
for _ in range(30):
 pop=sorted(pop,key=lambda x:x*x,reverse=True); elite=pop[:4]; pop=elite+[max(0,min(31,random.choice(elite)+random.randint(-3,3))) for _ in range(8)]
best=max(pop,key=lambda x:x*x); print('Best x:',best,'f(x):',best*best)
