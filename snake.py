UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self, position, direction):
        self.body = position
        self.direction = direction

    def get_body(self):
        return self.body

    def take_step(self, position):
        self.body = self.body[1:] + position

    def head(self):
        return self.body[-1]

    def set_direction(self, direction):
        self.direction= direction

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
        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], UP)

    def render(self):
        def print_boundaries(width):
            print("+", end="")
            print("-" * width, end="")
            print("+")

        # TODO: clean up (this is ugly)
        print_boundaries(self.width)
        snake_body = self.snake.get_body()
        for i in range(self.height):
            print("|", end="")
            for j in range(self.width):
                empty_cell = True
                for k in range(len(snake_body)):
                    if (i, j) == snake_body[k]:
                        empty_cell = False
                        if k == len(snake_body) - 1:
                            print("x", end="")
                        else:
                            print("o", end="")
                if empty_cell:
                    print(" ", end="")
            print("|")
        print_boundaries(self.width)
        

game = Game(20, 20)
game.render()
