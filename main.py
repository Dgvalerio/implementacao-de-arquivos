class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)


class List:
    def __init__(self):
        self.start = None

    def __repr__(self):
        return "[" + str(self.start) + "]"

    # Para inserir no inicio da lista
    def unshift(self, new_data):
        node = Node(new_data)
        node.next = self.start
        self.start = node


if __name__ == '__main__':
    list = List()
    list.unshift(8)
    print(list)
    list.unshift(16)
    print(list)
