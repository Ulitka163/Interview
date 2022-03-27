class Stack:
    def __init__(self, stack):
        self.stack = stack

    def isEmpty(self):
        if len(self.stack) == 0:
            return True

    def push(self, element):
        element + self.stack

    def pop(self):
        if self.isEmpty():
            return None
        pop_element = self.stack[0]
        self.stack = self.stack[1:]
        return pop_element

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)


def stack_valid(str):
    start = {1: '(', 2: '{', 3: '['}
    end = {1: ')', 2: '}', 3: ']'}
    stack_1 = Stack(str)
    if stack_1.size() % 2 == 0:
        stack_list = list(str)
        index = 1
        for a in stack_list[index-1:]:
            for key, values in end.items():
                if a == values:
                    index = stack_list.index(a)
                    if stack_list[index - 1] == start[key]:
                        stack_list.pop(index)
                        stack_list.pop(index-1)
                    else:
                        return print('Несбалансированно')
        return print('Сбалансировано')
    else:
        return print('Несбалансированно')


if __name__ == '__main__':
    string_ = input('Введите строку: ')
    stack_valid(string_)
