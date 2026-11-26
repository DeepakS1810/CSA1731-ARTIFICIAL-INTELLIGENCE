from math import dist
train=[((1,1),'A'),((1,2),'A'),((4,4),'B'),((5,4),'B')]; point=(3,3); k=3
nearest=sorted(train,key=lambda row:dist(row[0],point))[:k]; votes={c:sum(label==c for _,label in nearest) for c in {label for _,label in nearest}}
print('Neighbors:',nearest); print('Predicted class:',max(votes,key=votes.get))
