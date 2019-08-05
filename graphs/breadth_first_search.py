"""
Depth-first search is simple: 

1. Take a *stack* 
2. Add node to stack
3. Pop from stack
3. Add node's children to stack
4. Repeat until stack is empty

The stack guarantees we visit children before sibling nodes by virtue of its FILO properties.

Common interview modifications:

- Store some metadate along with the node e.g. stack = [(metadata, node)] instead.
- Handle cyclic graphs through use of a `visited_nodes` set, and refuse to add any children also in the `visited_nodes` set to the stack.
"""

def depth_first_search(node):

    stack = [node]

    while stack:
        # remove the last element - it's a stack, remember?
        current_node = stack.pop(0)
        if current_node.children:
            # add children to stack
            stack += current_node.children 

    return # whatever you want
