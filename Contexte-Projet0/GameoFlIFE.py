# grid : matrice 2d
# width : int
# height : int


# init (width, height, i)
# randomize()
# process()
# resize(width, height)
# get_cell(w, h)
# set_cell(w, h, v)
import random

class GOLEngline:
    
    i = 1 # i = initial state (1 ou 0/true or false)
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.i = 1
        
        
        self.__grid = self.initializeGrid()
        self.__temp = []
        
    
    def initializeGrid(self):
        return [[random.randint(0,self.i) for _ in range(self.__width)] for _ in range(self.__height)]
        
    def randomizer(self):
        random.shuffle(self.__grid)
        
    def process(self):
        temp_grid = [[0 for _ in range(self.__width)] for _ in range(self.__height)]
        
        for y in range(self.__width - 1):
            for x in range(self.__height - 1):
                cell_voisins = sum([self.get_cell(x-1, y-1), self.get_cell(x, y-1), self.get_cell(x+1, y-1),
                                self.get_cell(x-1, y),                            self.get_cell(x+1, y),
                                self.get_cell(x-1, y+1), self.get_cell(x, y+1), self.get_cell(x+1, y+1)
                                ])

                if self.get_cell(x, y) == 1: # donc en vie
                    if cell_voisins < 2 or cell_voisins > 3:
                        temp_grid[y][x] = 0
                    else:
                        temp_grid[y][x] = 1
                else: # donc mort
                    if cell_voisins == 3:
                        temp_grid[y][x] = 1 # La cellule devient en vie

        
        self.__grid = temp_grid # Inversement des tableau par changement d'adresse

                
                
                
                
            
    
    def resize(self, width, height):
        if 3 <= width <= 2500 and 3 <= height <= 2500:
                self.__height = height
                self.__width = height
                self.__grid = self.initializeGrid()
        
    def get_cell(self, x, y):
        if 0 <= x < self.__width and 0 <= y < self.__height:
            return self.__grid[x][y]
        else: 
            print('Erreur')
        return 0
    
    def set_cell(self, width, height, value):
        if 0 <= width < self.__width and 0 <= height < self.__height:
            self.__grid[width][height] = value
     
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.width =  max(0, value)
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.height = max(0, value)

        

gol = GOLEngline(10, 9)

def main():
    gol.randomizer()
    print(f'World {gol.width} x {gol.height}')

    gol.process()

    gol.width = 100
    gol.process()
    gol.resize(100, 100)

if __name__ == '__main__':
    main()
