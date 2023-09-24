# Como a idea é simular uma memória de 32 bytes, irei deixar o tamanho da lista limitada com essa variável

memorySize = 32


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

    def verify_empty_space(self, size):
        head = None
        count = 0
        for index, value in enumerate(self.memory):
            if value is None:
                if head is None:
                    head = index
                count += 1
                if count >= size:
                    return head
            else:
                head = None
        return None

#todo: guarda a posição do próximo item e talvez as heads
    def add_file(self, file):
        start_index = self.verify_empty_space(len(file))
        if start_index is None:
            return print('Memory our of range!!!', file, "can't be inserted")
        for index, letter in enumerate(file):
            self.memory[start_index+index] = letter
        print(self.memory)


if __name__ == '__main__':
    disk = Disk()
    disk.add_file('Pernambuco')
    disk.add_file('São Paulo')
    # disk.add_file('São Alagoas')
    # disk.add_file('Santa Catarina')
