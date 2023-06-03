''' 
Read a directed graph with two vertices
and edge's weight between them.
Test Case:
3
Dhaka Mymensign 140
Dhaka Gazipur 70
Gazipur Tangail 50
'''

from collections import defaultdict

edges = int(input("Number of edges:"))

graph = defaultdict(dict)

for _ in range(edges):
    u, v, weight = input().split()
    graph[u][v] = int(weight)

# Traverse the graph (Depth-first Search)
def dfs(node, visited):
    visited.add(node)
    print(node.title(), end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited) # recursive approach
    

# Start Traversal

# Keep tract of the visiting nodes
visited = set()

# List out of keys in graph
# and [0] is the first element of that list
# returns the first key in the dictionary.
dfs(list(graph.keys())[0], visited) 

print("Traveled.")




























