# array of edges
n=4
A=[[1,2],[2,3],[3,4],[4,1]]

# adjacency matric
m=[]
# creates an empty adjacency matrix
for i in range(n):
    m.append([0]*n)
for u,v in A:
    m[u][v]=1
    # if undirected i mean bidirectional
    m[v][u]=1

# convert the array of edges into adjacency list
from collections import defaultdict

d=defaultdict(list)
for u,v in A:
    d[u].append(v)
    # for undirected 
    d[v].append(u)

# depth first search recursive
# time complexity O(E+v)

def dfs_recursive(node):
    print(node)
    for neighbours in d[node]:
        if neighbour not in seen_list:
            seen_list.append(node)
            dfs_recursive(neighbour)
source=0
seen_list=set()
seen_list.add(source)
dfs_recursive(source)

# iterative DFS with a stack
source=0
seen_lsit=set()
stack=[source]

while stack:
    node=stack.pop()
    for neigh in D[node]:
        if neigh not in seen_list:
            seen_list.add(neigh)
            stack.append(neigh)



# breadth first search
from collections import deque

d=deque()
d.append(source)


while d:
    node=d.popleft()
    for neigh in D[node]:
        seen_list.add(neigh)
        d.append(neigh)




    
