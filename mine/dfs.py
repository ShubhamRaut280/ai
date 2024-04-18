


def dfs(graph, start):
	visited = set()
	stack = [start]

	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			print(vertex, end=' ')

		for neighbour in graph[vertex]:
			if neighbour not in visited : 
				stack.append(neighbour)



def bfs(graph, start):
	visited = set()
	queue = [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited : 
			visited.add(vertex)
			print(vertex , end = ' ')
		
		for neighbour in graph[vertex]:
			if neighbour not in visited:
				queue.append(neighbour)


graph={};
vertices = int(input("Enter number of vertices : "))
for i in range(vertices):
	vertex = (input("Enter vertex : "))
	othernebours = (input("Enter its neighbours space seperated: ").split())
	graph[vertex] = othernebours

start = input("Enter the start vertex : ")
print("DFS res : ")
dfs(graph, start)
print()

print("BFS res: ")
bfs(graph, start)



