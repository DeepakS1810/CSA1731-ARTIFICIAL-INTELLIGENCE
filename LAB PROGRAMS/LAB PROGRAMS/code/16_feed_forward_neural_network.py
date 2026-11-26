# Tiny feed-forward network trained with NumPy on XOR.
import numpy as np
X=np.array([[0,0],[0,1],[1,0],[1,1]],float); y=np.array([[0],[1],[1],[0]],float); rng=np.random.default_rng(2)
W1=rng.normal(size=(2,4)); b1=np.zeros((1,4)); W2=rng.normal(size=(4,1)); b2=np.zeros((1,1)); sig=lambda z:1/(1+np.exp(-z))
for _ in range(12000):
 h=sig(X@W1+b1); o=sig(h@W2+b2); dz=o-y; d2=dz*o*(1-o); d1=(d2@W2.T)*h*(1-h); W2-=.8*h.T@d2/4; b2-=.8*d2.mean(0); W1-=.8*X.T@d1/4; b1-=.8*d1.mean(0)
print('XOR predictions:',(sig(sig(X@W1+b1)@W2+b2).ravel()>.5).astype(int).tolist())
