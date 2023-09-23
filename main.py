# Considere a implementação de arquivos com lista encadeada.
# Um arquivo é dividido em vários blocos encadeados no disco.
# Cada bloco deve possuir o tamanho de 1 byte (uma letra) e um ponteiro para o bloco seguinte,
# sendo o último bloco com ponteiro nulo indicando seu final.
class Block:
    def __init__(self, letter=0, next_block=None):
        self.letter = letter
        self.next = next_block

    def __repr__(self):
        return '%s -> %s' % (self.letter, self.next)


class File:
    def __init__(self):
        self.start = None

    def __repr__(self):
        return "[" + str(self.start) + "]"

    # Para inserir no inicio da lista
    def unshift(self, new_data):
        node = Block(new_data)
        node.next = self.start
        self.start = node


if __name__ == '__main__':
    file = File()
    file.unshift(8)
    print(file)
    file.unshift(16)
    print(file)
