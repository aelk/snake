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
    def __init__(self):
        self.board = []
        self.points = 0

    def initialize_board(self, height, width):
        # TODO
        return self.board

    def render_board():
        # TODO
        return
        
