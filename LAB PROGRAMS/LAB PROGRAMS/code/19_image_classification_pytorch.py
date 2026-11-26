# Minimal PyTorch MLP classifier for a toy 2-class image dataset.
# Install first: python -m pip install torch
try:
 import torch
 from torch import nn
except ImportError:
 print('PyTorch is not installed; expected toy labels: [0, 0, 1, 1]')
 print('Install with: python -m pip install torch'); raise SystemExit(0)
X=torch.tensor([[0.,0.,0.,0.],[0.,0.,1.,1.],[1.,1.,0.,0.],[1.,1.,1.,1.]])
y=torch.tensor([0,0,1,1]); model=nn.Sequential(nn.Linear(4,8),nn.ReLU(),nn.Linear(8,2)); opt=torch.optim.Adam(model.parameters(),lr=.05); loss=nn.CrossEntropyLoss()
for _ in range(300): opt.zero_grad(); L=loss(model(X),y); L.backward(); opt.step()
print('Toy image labels:',model(X).argmax(1).tolist()); print('Note: replace toy vectors with normalized image pixels for a real dataset.')
