graph={'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':['F'],'F':[]}
def dfs(node,seen):
 if node in seen:return
 seen.add(node); order.append(node)
 for nxt in graph[node]: dfs(nxt,seen)
order=[]; dfs('A',set())
print('DFS visit order:', ' -> '.join(order))
