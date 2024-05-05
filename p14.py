class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dest, cost):
        for node in [src, dest]:
            self.graph.setdefault(node, [])
        self.graph[src].append((dest, cost))
        self.graph[dest].append((src, cost))  

    def dfs(self, start, visited):
        visited.add(start)
        [self.dfs(neighbor, visited) for neighbor, _ in self.graph[start] if neighbor not in visited]

    def is_connected(self):
        visited = set()
        self.dfs(next(iter(self.graph)), visited)
        return len(visited) == len(self.graph)

    def adjacency_matrix(self):
        nodes = sorted(self.graph.keys())
        matrix = [[float('inf')] * len(nodes) for _ in nodes]
        indices = {node: i for i, node in enumerate(nodes)}

        for node, edges in self.graph.items():
            for neighbor, cost in edges:
                matrix[indices[node]][indices[neighbor]] = cost

        return matrix, nodes

def take_input():
    g = Graph()
    for _ in range(int(input("Enter the number of flight connections: "))):
        src, dest, cost = [input(f"Enter {s}: ").strip().upper() for s in ("source city/airport", "destination city/airport", "the cost")]
        g.add_edge(src, dest, float(cost))
    return g

def main():
    g = take_input()
    print("The graph is" + [" not", ""][g.is_connected()] + " connected.")
    matrix, nodes = g.adjacency_matrix()
    print("\nAdjacency Matrix:")
    print("\t" + "\t".join(nodes))
    for i, row in enumerate(matrix):
        print(nodes[i], end="\t")
        for cost in row:
            print(cost if cost != float('inf') else "-", end="\t")
        print()

if __name__ == "__main__":
    main()
