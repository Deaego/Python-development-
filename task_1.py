class Matrix():
    def __init__(self, data):
        self.data = data
        for line in self.data[:1]:
            if not len(line) == len(self.data[self.data.index(line) + 1]):
                raise ValueError('Колличество элементов в строках не верное')
            
    def __str__(self):
        return'\n'.join('\t'.join(str(num) for num in line) for line in self.data)

    def __add__(self, other):
        if not len(self.data) == len(other.data):
            raise ValueError('Размерности матриц не совпадают')
        else:
            for i in range(len(self.data)):
                if not len(self.data[i]) == len(other.data[i]):
                    raise ValueError('Размерности матриц не совпадают')
            item = [[int(self.data[line][num]) + int(other.data[line][num]) for num in
                     range(len(self.data[line]))] for line in range(len(self.data))]
            return Matrix(item)


m_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
mtr_1 = Matrix(m_1)
mtr_2 = Matrix(m_2)
print(mtr_1)
print(mtr_2)
print(mtr_1 + mtr_2)
