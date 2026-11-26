# Linear SVM by hinge-loss gradient descent on a tiny separable dataset.
X=[(-2,-1),(-1,-2),(1,2),(2,1)]; y=[-1,-1,1,1]; w=[0.,0.]; b=0.; lr=.01; C=1
for _ in range(2000):
 gw=[w[0],w[1]]; gb=0
 for (x1,x2),t in zip(X,y):
  if t*(w[0]*x1+w[1]*x2+b)<1: gw[0]-=C*t*x1; gw[1]-=C*t*x2; gb-=C*t
 w[0]-=lr*gw[0]; w[1]-=lr*gw[1]; b-=lr*gb
print('Linear SVM weights:',[round(v,2) for v in w],'bias:',round(b,2)); print('Training predictions:',[1 if w[0]*x[0]+w[1]*x[1]+b>=0 else -1 for x in X])
