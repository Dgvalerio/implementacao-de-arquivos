# Como a idea é simular uma memória de 32 bytes, irei deixar o tamanho da lista limitada com essa variável
memory_size = 32


class Disk:
    memory = [None] * memory_size
    heads = []

    def show_memory(self):
        print(f'Index\tBlock\tNext')
        for index, block in enumerate(self.memory):
            if block is None:
                print(f'{index}\t\t{block}\t{block}')
            else:
                print(f'{index}\t\t{block[0]}\t\t{block[1]}')
        print('')

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

        if start_index is None:
            return print(f'Falha!\nO arquivo "{file}" excede o tamanho da memória!\n')

        self.heads.append(start_index)

        saved = 0
        last = 0

        for index in range(memory_size):
            if self.memory[index] is None:
                if saved > 0:
                    self.memory[last][1] = index
                last = index
                self.memory[index] = [file[saved], None]
                saved += 1
            if saved == len(file):
                break

    def get_file(self, head):
        block = self.memory[head]
        if block[1] is None:
            return f'{block[0]}'
        else:
            next_block = self.get_file(block[1])
            return f'{block[0]}{next_block}'

    def remove_block(self, block_index):
        next_block = self.memory[block_index][1]
        self.memory[block_index] = None
        if next_block is not None:
            self.remove_block(next_block)

    def remove_file(self, file):
        for head in self.heads:
            memory_file = self.get_file(head)
            if file == memory_file:
                self.remove_block(head)
                return print(f'Arquivo "{file}" deletado!\n')
        print(f'Arquivo "{file}" não foi encontrado na memória!\n')


if __name__ == '__main__':
    disk = Disk()

    disk.add_file('Pernambuco')
    disk.show_memory()

    disk.add_file('São Paulo')
    disk.show_memory()

    disk.add_file('Alagoas')
    disk.show_memory()

    disk.add_file('Santa Catarina')
    disk.show_memory()

    disk.remove_file('São Paulo')
    disk.show_memory()

    disk.add_file('Santa Catarina')
    disk.show_memory()
