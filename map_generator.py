
class MapGenerator():
    def __init__(self, game):
        self.game = game
        self.map_gen = []
        self.map_size = (12, 12)
        self.map_x, self.map_y = self.map_size
        self.map_xs, self.map_ys = self.map_x - 1, self.map_y - 1
        #self.generate_map()
        self._ = False

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
                    elif column == self.map_x:
                        row_list.append(1)
                    else:
                        row_list.append(self._)
                else:
                    row_list.append(1)
            self.map_gen.append(row_list)

        #debug
        #for row in self.map_gen:
        #    print(row)

        return(self.map_gen)

