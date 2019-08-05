def in_order(root):

    if root is None:
        return []

    return in_order(root.left) + [root.value] + in_order(root.right)

def pre_order(root):

    if root is None:
        return []

    return [root.value] + pre_order(root.left) + pre_order(root.right)

def post_order(root):

    if root is None:
        return []

    return post_order(root.left) + post_order(root.right) + [root.value]
