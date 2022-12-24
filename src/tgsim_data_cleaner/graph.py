import numpy as np

# Finds and returns a car's initial ID given changed ID
def FindRootId(id, graph):
    if id not in graph:
        return np.nan
    current_id = id
    while len(graph[current_id]) > 0:
        current_id = graph[current_id][0]
    return current_id


# Is id1 connected to id2?
def IsConnected(id1, id2, graph):
    if id1 not in graph or id2 not in graph:
        return False

    visited = [id1]
    queue = [id1]
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        if m == id2:
            return True
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return False
