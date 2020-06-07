import os
import random

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)
APPLE_SYMBOL = '&'

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
        self.direction = direction

    def move_to_direction(self, move):
        wsadMap = {
            'w': UP,
            's': DOWN,
            'a': LEFT,
            'd': RIGHT
        }
        return wsadMap[move.lower()]

    def get_new_head_position(self, move):
        head_x, head_y = self.head()
        x, y = self.move_to_direction(move)
        return (head_x - y, head_y + x)

    def extend(self, move):
        new_head_x, new_head_y = self.get_new_head_position(move)
        x, y = self.move_to_direction(move)
        self.body = [(new_head_x - y, new_head_y + x)] + self.body

class Apple:
    def __init__(self, board_height, board_width):
        self.location = self.get_random_apple(board_height, board_width)

    def get_random_apple(self, height, width):
        return (random.randint(0, height - 1), random.randint(0, width - 1))

    def get_location(self):
        return self.location

class Game:
    def __init__(self, height, width):
        self.score = 0
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
                if self.board[i][j] is not None:
                    print(self.board[i][j], end="")
                    continue
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
        print("Score:", self.score)

    def is_illegal_move(self, move):
        move = str(move)
        if move is None or len(move) != 1 or move not in 'WwSsAaDd':
            print("Illegal move. Exiting...")
            return True
        return False

    def is_self_collision(self, new_pos):
        if new_pos in self.snake.get_body()[:-1]:
            print("Ouch! You ran into yourself. Exiting...")
            return True
        return False
    
    def is_border_collision(self, move, new_pos):
        x, y = new_pos
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            print("Hit the border. Exiting...")
            return True
        return False

    def make_move(self, move):
        if self.is_illegal_move(move):
            return False

        new_head_pos = self.snake.get_new_head_position(move)
        if self.is_self_collision(new_head_pos) or \
            self.is_border_collision(move, new_head_pos):
            return False

        x, y = new_head_pos
        if self.board[x][y] == APPLE_SYMBOL:
            self.board[x][y] = None
            self.snake.extend(move)
            self.place_apple()
            self.score += 1

        self.snake.take_step([new_head_pos])
        return True

    def place_apple(self):
        self.apple = Apple(self.height, self.width)
        apple_x, apple_y = self.apple.get_location()
        self.board[apple_x][apple_y] = APPLE_SYMBOL

    def play(self):
        self.place_apple()
        self.render()
        while True:
            move = str(input("Make a move (WSAD): "))
            move_result = self.make_move(move)
            if move_result is False:
                break

            os.system('clear')
            self.render()

if __name__ == '__main__':
    game = Game(10, 30)
    game.play()
