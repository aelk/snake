class Snake:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def set_position(self, pos):
        self.position = pos

    def get_position(self):
        return self.position

    def set_direction(self, direction):
        self.direction= direction

    def get_direction(self):
        return self.direction

class Apple:
    def __init__(self, location):
        self.location = location

    def get_location(self):
        return self.location

class Game:
    def __init__(self, height, width):
        self.points = 0
        self.height = height
        self.width = width
        self.board = [[None for i in range(width)] for j in range(height)]

    def render(self):
        def print_boundaries(width):
            print("+", end="")
            print("-" * width, end="")
            print("+")

        print_boundaries(self.width)
        for i in range(self.height):
            print("|", end="")
            for j in range(self.width):
                if self.board[i][j] is not None:
                    print(self.board[i][j], end="")
                else:
                    print(" ", end="")
            print("|")
        print_boundaries(self.width)
        

game = Game(20, 20)
game.render()
