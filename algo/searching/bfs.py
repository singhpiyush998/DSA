class Graph:
    def __init__(self, paths):
        self.paths = paths
    
    def neighbours(self, vertex):
        return self.paths[vertex]

    def __len__(self):
        return len(self.paths)

def visit(v):
    print(v, end=" ")

def bfs(G, v):
    marked = [False] * len(G)

    queue = [v]
    while len(queue) > 0:
        v = queue.pop(0)
        if not marked[v]:
            visit(v)
            marked[v] = True

            for w in G.neighbours(v):
                if not marked[w]:
                    queue.append(w)

    print()
    

def main():
    paths = {
        0: [1, 3, 2],
        1: [3, 0],
        2: [3, 0],
        3: [1, 2, 4],
        4: [3]
    }

    graph = Graph(paths)

    bfs(graph, 0)

if __name__ == "__main__":
    main()
