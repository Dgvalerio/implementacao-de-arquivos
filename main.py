# Como a idea é simular uma memória de 32 bytes, irei deixar o tamanho da lista limitada com essa variável
memorySize = 32


class Block:
    def __init__(self, letter, next_block=None):
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


class Disk:
    memory = [None] * memorySize
    heads = []

    def __repr__(self):
        print(f'Index\tBlock\tNext')
        for index, block in enumerate(self.memory):
            if block is None:
                print(f'{index}\t\t{block}\t{block}')
            else:
                print(f'{index}\t\t{block[0]}\t\t{block[1]}')
        return ""

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
        return None

    def add_file(self, file):
        start_index = self.verify_empty_space(len(file))
        self.heads.append(start_index)
        if start_index is None:
            return print(f'Falha! O arquivo "{file}" excede o tamanho da memória!')

        saved = 0
        last = 0

        for index in range(memorySize):
            if self.memory[index] is None:
                if saved > 0:
                    self.memory[last][1] = index
                last = index
                self.memory[index] = [file[saved], None]
                saved += 1
            if saved == len(file):
                break


if __name__ == '__main__':
    disk = Disk()
    disk.add_file('Pernambuco')
    print(disk)
    disk.add_file('São Paulo')
    print(disk)
    disk.add_file('Alagoas')
    print(disk)

    disk.add_file('Santa Catarina')
    print(disk.heads)
