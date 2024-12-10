from collections import defaultdict
class Graph:
    def __init__(self):
        self.value = defaultdict(list)  
    def drawGraph(self, parent, child):
        self.value[parent].append(child)  
    def DFS(self, start):
        visited = [] 
        stack = [start]  
        print("DFS Traversal:", end=" ")
        while stack:
            s = stack.pop()  
            if s not in visited:
                print(s, end=" ") 
                visited.append(s) 
                for neighbor in reversed(self.value[s]):  
                    if neighbor not in visited:
                        stack.append(neighbor)

    def BFS(self, start):
        visited = []  
        queue = [start]  

        print("\nBFS Traversal:", end=" ")

        while queue:
            x = queue.pop(0) 
            if x not in visited:
                print(x, end=" ")  
                visited.append(x)  

                for neighbor in self.value[x]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Create a graph and add edges.
g = Graph()
g.drawGraph(1, 4)
g.drawGraph(1, 2)
g.drawGraph(2, 3)
g.drawGraph(2, 6)
g.drawGraph(4, 5)
g.drawGraph(4, 7)
g.drawGraph(7, 96)

# Perform DFS and BFS traversals.
g.DFS(1)
g.BFS(1)
