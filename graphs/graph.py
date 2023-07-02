graph = dict()

def addEdge(node1, node2):
    # create an empty list for a key node
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []

    # append the neighbor node to its corresponding key node 
    graph[node1].append(node2)


def main():
    addEdge('A', 'B')
    addEdge('A', 'C')
    addEdge('B', 'D')
    addEdge('B', 'E')
    addEdge('C', 'D')
    addEdge('D', 'A')
    addEdge('D', 'E')

    for key, val in graph.items():
        print(f"{key}-->{val}")
        
if __name__=="__main__":
    main()