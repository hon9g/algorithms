from collections import defaultdict
from collections import deque

def build_graph(E):
	G = defaultdict(list)
	for _ in range(E):
		v1, v2 = [int(x) for x in input().split(" ")]
		G[v1].append(v2)
		G[v2].append(v1)
	for key, val in G.items():
		G[key] = sorted(val)
	return G

def DFS(G, v_start):
	visited, stack, path = set(), [v_start], []
	while stack:
		v = stack.pop()
		if v not in visited:
			visited.add(v)
			path.append(v)
			stack += reversed(G[v])
	return path

def BFS(G, v_start):
	visited, queue, path = set(), deque([v_start]), []
	while queue:
		v = queue.popleft()
		if v not in visited:
			visited.add(v)
			path.append(v)
			queue += G[v]
	return path

if __name__ == "__main__":
	num_V, num_E, v_start = [int(x) for x in input().split(" ")]
	graph = build_graph(num_E)
	dfs = " ".join(str(x) for x in DFS(graph, v_start))
	bfs = " ".join(str(x) for x in BFS(graph, v_start))
	print(dfs)
	print(bfs)