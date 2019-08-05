"""
Breadth-first search is simple: 

1. Take a *queue* 
2. Add node to queue
3. Pop from queue
3. Add node's children to queue
4. Repeat until queue is empty

Common interview modifications:

- Store some metadate along with the node e.g. queue = [(metadata, node)] instead.
- Handle cyclic graphs through use of a `visited_nodes` set, and refuse to add any children also in the `visited_nodes` set to the queue.
"""

def breadth_first_search(node):

    queue = [node]

    while queue:
        # remove the first element - it's a queue, remember?
        current_node = queue.pop(0)
        if current_node.children:
            # add children to queue
            queue += current_node.children 

    return # whatever you want
