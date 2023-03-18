from random import randint

class Graph:
    def __init__(self, paths):
        self.paths = paths
    
    def neighbours(self, vertex):
        return self.paths[vertex]

    def __len__(self):
        return len(self.paths)

def visit(v):
    print(v, end=" ")

def dfs_post(G, v):
    global marked
    marked[v] = True
    for w in G.neighbours(v):
        if not marked[w]:
            dfs_pre(G, w)

    visit(v)

marked = []
def dfs_pre(G, v):
    visit(v)
    global marked
    marked[v] = True
    for w in G.neighbours(v):
        if not marked[w]:
            dfs_pre(G, w)


def dfs_iter(G, v):
    pass

def main():
    paths = {
        0: [1, 3, 2],
        1: [3, 0],
        2: [3, 0],
        3: [1, 2, 4],
        4: [3]
    }

    graph = Graph(paths)
    l = list(paths)
    arbitrary_vertex = l[randint(0, len(l) - 1)]

    global marked
    marked = [False] * len(graph)

    # dfs_pre(graph, 0)
    dfs_post(graph, arbitrary_vertex)
    # dfs_iter(graph, 0)

if __name__ == "__main__":
    main()
