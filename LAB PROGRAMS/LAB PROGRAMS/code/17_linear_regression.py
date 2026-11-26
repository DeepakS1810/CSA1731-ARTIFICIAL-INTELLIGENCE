# Least-squares linear regression using Python only.
x=[1,2,3,4,5]; y=[3,5,7,9,11]; n=len(x); mx=sum(x)/n; my=sum(y)/n
m=sum((a-mx)*(b-my) for a,b in zip(x,y))/sum((a-mx)**2 for a in x); b=my-m*mx
print(f'Model: y = {m:.1f}x + {b:.1f}'); print('Prediction at x=6:',m*6+b)
