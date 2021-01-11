class BinaryTree:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key, value, position, ref_node=None, is_referenced=False):
        ref_node = ref_node if is_referenced else self
        if ref_node is None:
            return
        if key == ref_node.value:
            if position == "left":
                if ref_node.left is None:
                    ref_node.left = BinaryTree(value=value)
                else:
                    return "Node Already Exist."
            elif position == "right":
                if ref_node.right is None:
                    ref_node.right = BinaryTree(value=value)
                else:
                    return "Node Already Exist."
        else:
            ref_node.insert(key=key, value=value, position=position, ref_node=ref_node.left, is_referenced=True)
            ref_node.insert(key=key, value=value, position=position, ref_node=ref_node.right, is_referenced=True)

    def search(self, key, ref_node=None, is_referenced=False):
        ref_node = ref_node if is_referenced else self
        if ref_node is None:
            return
        if key == ref_node.value:
            return "Found."
        else:
            ref_node.search(key=key, ref_node=ref_node.left, is_referenced=True)
            ref_node.search(key=key, ref_node=ref_node.right, is_referenced=True)

    def display(self, ref_node=None, is_referenced=False):
        data = []
        ref_node = ref_node if is_referenced else self
        if ref_node is None:
            return
        else:
            data.append(ref_node.value)
        ref_node.display(ref_node=ref_node.left, is_referenced=True)
        ref_node.display(ref_node=ref_node.right, is_referenced=True)
