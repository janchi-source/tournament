import pygame as pg

# setting up numbers
pg.init()

BLACK = (0,0,0)
GRAY = (80,80,80)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SIDE = 50
tile_width = SIDE
tile_heigth = SIDE
margin = 0
cells = []
screen = 850


win = pg.display.set_mode((screen, screen))
max_w = (pg.display.get_surface().get_width() - margin) // (tile_width+margin)
max_h = (pg.display.get_surface().get_height() - margin) // (tile_heigth+margin)
win.fill(GRAY)
clock = pg.time.Clock()


player1_pos = (1, 7)
player2_pos = (15, 7)

finish1_pos = (5, 15)
finish2_pos = (7, 1)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# left = (0, 0, 0, 1)
# right = (0, 1, 0, 0)
# up = (1, 0, 0, 0)
# down = (0, 0, 1, 0)
# empty = (0, 0, 0, 0)


# world_data = [empty, up, up, up, up, up, up, empty,
#               left, empty, empty, empty, empty, empty, empty, right,
#               left, empty, empty, empty, empty, empty, empty, right,
#               left, empty, empty, empty, empty, empty, empty, right,
#               left, empty, empty, empty, empty, empty, empty, right,
#               left, empty, empty, empty, empty, empty, empty, right,
#               left, empty, empty, empty, empty, empty, empty, right,
#               empty, down, down, down, down, down, down, empty,]

world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 8, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 9, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]




def draw_cells():
    for y, row in enumerate(world_data):
        for x, cell in enumerate(row):
            if cell == 1:
                pg.draw.rect(win, BLACK, (x * SIDE, y * SIDE, SIDE, SIDE))
            if cell == 8:
                pg.draw.rect(win, RED, (x * SIDE, y * SIDE, SIDE, SIDE))
            if cell == 9:
                pg.draw.rect(win, GREEN, (x * SIDE, y * SIDE, SIDE, SIDE))


def draw_entities():
    pg.draw.rect(win, WHITE, (player1_pos[0] * SIDE, player1_pos[1] * SIDE, SIDE, SIDE))
    pg.draw.rect(win, WHITE, (player2_pos[0] * SIDE, player2_pos[1] * SIDE, SIDE, SIDE))
    pg.draw.rect(win, RED, (finish1_pos[0] * SIDE, finish1_pos[1] * SIDE, SIDE, SIDE))
    pg.draw.rect(win, GREEN, (finish1_pos[0] * SIDE, finish1_pos[1] * SIDE, SIDE, SIDE))



def move_player(player_pos, direction):
    new_pos = (player_pos[0] + direction[0], player_pos[1] + direction[1])
    if world_data[new_pos[1]][new_pos[0]] == 0:
        return new_pos
    else:
        return player_pos







# def gen_cells():
#     for col in range(max_w):
#         x = margin + col * (tile_heigth + margin)
#         cells.append([])
#         for row in range(max_h):
#             y = margin + row * (tile_width + margin)
#             rect = pg.Rect(x, y, tile_width, tile_heigth)
#             pg.draw.rect(win, BLACK, rect)
#             y += tile_heigth + margin
#             cells[col].append(rect)
#         x += tile_width + margin

def main():
    draw_cells()
    draw_entities()
    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:  # check for exit
                running = False
            if e.type == pg.MOUSEBUTTONUP and e.button == 1:  # on mouse click
                x, y = e.pos
                for row in cells:
                    for rect in row:
                        if rect.collidepoint(x, y):
                            pg.draw.rect(win, WHITE, rect)
        

        keys = pg.key.get_pressed()

        # Player 1 
        if keys[pg.K_w]:
            player1_pos = move_player(player1_pos, UP)
        if keys[pg.K_s]:
            player1_pos = move_player(player1_pos, DOWN)
        if keys[pg.K_a]:
            player1_pos = move_player(player1_pos, LEFT)
        if keys[pg.K_d]:
            player1_pos = move_player(player1_pos, RIGHT)

        # Player 2 
        if keys[pg.K_UP]:
            player2_pos = move_player(player2_pos, UP)
        if keys[pg.K_DOWN]:
            player2_pos = move_player(player2_pos, DOWN)
        if keys[pg.K_LEFT]:
            player2_pos = move_player(player2_pos, LEFT)
        if keys[pg.K_RIGHT]:
            player2_pos = move_player(player2_pos, RIGHT)


        # if player1_pos == exit_pos and player2_pos == exit_pos:
        #     winner = "It's a tie!"
        #     running = False
        # elif player1_pos == exit_pos:
        #     winner = "Player 1 wins!"
        #     running = False
        # elif player2_pos == exit_pos:
        #     winner = "Player 2 wins!"
        #     running = False

        pg.display.update()
            

    pg.quit()

if __name__ == "__main__":
    main()