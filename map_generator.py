import random

class MapGenerator():
    def __init__(self, game):
        self.game = game
        self._ = False
        self.map_x, self.map_y = 12, 12
        self.update()
        #self.generate_map()
        

    def generate_map(self):
        for row in range(self.map_y):
            row_list = []
            for column in range(self.map_x):
                if row == 0:                    #first row
                    row_list.append(1)
                elif row == self.map_ys:              #last row
                    row_list.append(1)
                elif row < self.map_y:               #middle rows
                    if column == 0 or column == self.map_xs: #sides
                        row_list.append(1)
                    else:
                        row_list.append(self._)
                        """
                        self.choice = random.randrange(4)
                        if self.choice == 0:
                            row_list.append(1)
                        elif self.choice == 1:
                            row_list.append(2)
                        elif self.choice == 2:
                            row_list.append(self._)
                        elif self.choice == 3:
                            row_list.append(self._)
                        """
                else:
                    row_list.append(1)
            self.map_gen.append(row_list)

        #debug
        #for row in self.map_gen:
        #    print(row)

        return(self.map_gen)

    def increase_map_size(self, numb):
        self.map_x = 12 + numb
        self.map_y = 12 + numb

    def update(self):
        self.map_gen = []
        self.map_xs, self.map_ys = self.map_x - 1, self.map_y - 1
        self.generate_map()