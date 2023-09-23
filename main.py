# Como a idea é simular uma memória de 32 bytes, irei deixar o tamanho da lista limitada com essa variável

memorySize = 8


class Block:
    def __init__(self, letter, next_block=None):
        self.letter = letter
        self.next = next_block

    def __repr__(self):
        return '%s -> %s' % (self.letter, self.next)


class Disk:
    memory = [None] * memorySize

    def __init__(self):
        self.start = None

    def __repr__(self):
        return "[" + str(self.start) + "]"

    # Para inserir no inicio da lista
    def unshift(self, new_data):
        node = Block(new_data)
        node.next = self.start
        self.start = node

    def verify_empty_space(self):
        empty = []
        for val in self.memory:
            print(val)

    def add_file(self, file):
        for index, letter in enumerate(file):
            if self.memory[index] is None:
                self.memory[index] = letter
            self.memory.append(letter)
        print(self.memory)


if __name__ == '__main__':
    disk = Disk()
    disk.add_file('Pernambuco')
    # disk.add_file('São Paulo')
    # disk.add_file('São Alagoas')
    # disk.add_file('Santa Catarina')
