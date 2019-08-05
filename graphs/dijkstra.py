"""
Dijkstra's algorithm requires total knowledge of all nodes ahead of time.

The algorithm is simple: 

1. Initialize an empty `visited` set. 
2. Initialize a `distances`dictionary, mapping each node to minimum distance from source node.
3. Set all values in `distances` to infinity.  
4. Set the source node's value in `distances` to 0.
5. Now, until all nodes are in the `visited set`:
	- Pick the node with smallest distance value. This is current node.
    - Update the `distances` value for all neighbours of the current node. 
        - The update rule: choose the minimum of current value or `distance[current_node] + travel distance from source to neighbour`

Common interview modifications:
"""

def dijkstra(graph, source):

	"""
	Assume `for node in graph` iterates over all nodes in graph.
    Assume graph[(A, B)] returns edge from A to B, if any
    """ 

    
    visited = set()
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    while True:

        # get a list of unvisited nodes. Once all nodes are visited, terminate. 
        unvisited_nodes = [node for node in graph if node not in visited]
        if not unvisited_nodes:
            break

        # pick the unvisited node with smallest `distance` value.
        smallest_node = min(unvisited_nodes, key=lambda node: distances[node]) 

        # update neighbours
        for node in smallest_node.neighbours:
            distances[node] = min(distances[node], distances[smallest_node] + graph[(smallest_node, node)])

        # ensure this node never goes through this loop again
        visited.add(smallest_node)

    return # whatever you want
