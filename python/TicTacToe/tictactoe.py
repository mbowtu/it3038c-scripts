import pygame as pg 
import sys
from random import randint

#setting up the size of the game window

WIN_SIZE = 700
CELL_SIZE = WIN_SIZE // 3
AB = float('inf')       # dfining fuction
vec2 = pg.math.Vector2  # defining a two dimensional vector
CELL_CENTER = vec2(CELL_SIZE / 2)

 # defining the game logic
class TicTacToe:
    def __init__(self, game):
        self.game = game

        # loading the images for the game.
        self.field_image = self.get_scaled_image(path='C:\Python310/field.png', res=[WIN_SIZE] * 2)
        self.O_image = self.get_scaled_image(path='C:\Python310/o.png', res=[CELL_SIZE] * 2)
        self.X_image = self.get_scaled_image(path='C:\Python310/x.png', res=[CELL_SIZE] * 2)
        
        # defining array for game field

        self.game_array = [[AB, AB, AB],
                           [AB, AB, AB],
                           [AB, AB, AB]]
        # random generator to determine which player (X or O) will go first
        self.player = randint(0, 1)

        self.line_indices_array = [[(0, 0), (0, 1), (0, 2)],
                                   [(1, 0), (1, 1), (1, 2)],
                                   [(2, 0), (2, 1), (2, 2)],
                                   [(0, 0), (1, 0), (2, 0)],
                                   [(0, 1), (1, 1), (2, 1)],
                                   [(0, 2), (1, 2), (2, 2)],
                                   [(0, 0), (1, 1), (2, 2)],
                                   [(0, 2), (1, 1), (2, 0)]]
        self.winner = None
        self.game_steps = 0

        # This will help display the winner in the game field screen
        self.font = pg.font.SysFont('Verdana', CELL_SIZE // 5, True)

    # defining fuction to check for the winner
    def check_winner(self):
        for line_indices in self.line_indices_array:
            sum_line = sum([self.game_array[i][j] for i, j in line_indices])
            if sum_line in {0, 3}:              
                self.winner = 'XO'[sum_line == 0] #if the sum equal to 0 then O is the winner, if the sum is equal to 3 then X is the winner.
                self.winner_line = [vec2(line_indices[0][::-1]) * CELL_SIZE + CELL_CENTER,
                                    vec2(line_indices[2][::-1]) * CELL_SIZE + CELL_CENTER]
    # method to run the game 
    def run_game_process(self):
        current_cell = vec2(pg.mouse.get_pos()) // CELL_SIZE
        col, row = map(int, current_cell)
        left_click = pg.mouse.get_pressed()[0]

        # getting the player move
        if left_click and self.game_array[row][col] == AB and not self.winner:
            self.game_array[row][col] = self.player
            self.player = not self.player
            self.game_steps += 1
            self.check_winner()

    # defining a method to display the gameplay
    def draw_objects(self):
        for y, row in enumerate(self.game_array):
            for x, obj in enumerate(row):
                if obj != AB:
                    self.game.screen.blit(self.X_image if obj else self.O_image, vec2(x, y) * CELL_SIZE)
   
    # defining a fuction to draw a line for the winner
    def draw_winner(self):
        if self.winner:
            pg.draw.line(self.game.screen, 'white', *self.winner_line, CELL_SIZE // 8)
            label = self.font.render(f'Player "{self.winner}" wins!', True, 'white', 'black')
            self.game.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 4))
    
    # funciton that will help display the gameplay field 
    def draw(self):
        self.game.screen.blit(self.field_image, (0, 0))
        self.draw_objects()
        self.draw_winner()

# Creating a static method to load and support image resolution

    @staticmethod
    def get_scaled_image(path, res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img, res) 

# displaying information about which player is making the first move and the result of the game
    def caption(self):
        pg.display.set_caption(f'Player "{"OX"[self.player]}" turn!')
        if self.winner:
            pg.display.set_caption(f'Player "{self.winner}" wins! Press Space to Restart')
        elif self.game_steps == 9:
            pg.display.set_caption(f'Game Over: draw! Press Space to Restart')

    def run(self):
        self.caption()
        self.draw()
        self.run_game_process()


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)   # screen resolution
        self.clock = pg.time.Clock()                 # setup the frame rate
        self.tic_tac_toe = TicTacToe(self)

# defining fuction to restart the game when pressing the space key
    def new_game(self):
        self.tic_tac_toe = TicTacToe(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.new_game()

# creating a loop for the game

    def run(self):
        while True:
            self.tic_tac_toe.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
