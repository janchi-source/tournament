import pygame as pg
import tilesmanger as tmg

# setting up numbers
pg.init()

BLACK = (0,0,0)
GRAY = (80,80,80)
WHITE = (255,255,255)
SIDE = 64
tile_width = SIDE
tile_heigth = SIDE
margin = 0
cells = []

win = pg.display.set_mode((768,768))
max_w = (pg.display.get_surface().get_width() - margin) // (tile_width+margin)
max_h = (pg.display.get_surface().get_height() - margin) // (tile_heigth+margin)
win.fill(GRAY)
clock = pg.time.Clock()
tm = tmg.tilesmanger(win)

def gen_cells():
    for col in range(max_w):
        x = margin + col * (tile_heigth + margin)
        cells.append([])
        for row in range(max_h):
            y = margin + row * (tile_width + margin)
            rect = pg.Rect(x, y, tile_width, tile_heigth)
            pg.draw.rect(win, BLACK, rect)
            y += tile_heigth + margin
            cells[col].append(tmg.tile(tm, rect, tmg.Direction.NONE))
        x += tile_width + margin

def main():
    gen_cells()
    cells[5][5].side = (tmg.Direction.UP,tmg.Direction.DOWN,tmg.Direction.LEFT,tmg.Direction.RIGHT)
    for row in cells:
        for tile in row:
            tile.handle_side()

    running = True
    while running:
        for e in pg.event.get(): 
            if e.type == pg.QUIT: # check for exit
                running = False
        if e.type == pg.MOUSEBUTTONUP and e.button == 1: # on mouse click
            x,y = e.pos
            for row in cells:
                for tile in row:
                    if tile.rect.collidepoint(x,y):
                        pg.draw.rect(win, WHITE, tile.rect)
        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()