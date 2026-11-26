# Simple two-room vacuum world agent.
rooms={'A':'Dirty','B':'Dirty'}; location='A'; actions=[]
for room in ('A','B'):
 location=room
 if rooms[room]=='Dirty': rooms[room]='Clean'; actions.append(f'Suck {room}')
 else: actions.append(f'Move to {room}')
print('Actions:', ' -> '.join(actions)); print('Final:', rooms)
