#List save map,and print the map(without __init__)
class Map:
    my_map = list()
    def set_map(self, n_arg):
        self.n = n_arg
        for i in range (0, self.n):
            a = list()
            for j in range (0, self.n):
                a.append('*')
                j += 1
            self.my_map.append(a)
            i += 1
    def set_pattern(self, p_arge):
        self.p = p_arge
        if p_arge == 1:
            initial_index = self.n // 2
            self.my_map[initial_index][initial_index - 1] = '0'
            self.my_map[initial_index - 1][initial_index - 1] = '0'
            self.my_map[initial_index - 1][initial_index] = '0'
            self.my_map[initial_index - 1][initial_index + 1] = '0'
            self.my_map[initial_index + 1][initial_index] = '0'
    def display(self):
        j = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                print(self.my_map[i][j],end = '')
                j += 1
            i += 1
            print(' ')
my_map = Map()
my_map.set_map(3)
my_map.set_pattern(1)
my_map.display()