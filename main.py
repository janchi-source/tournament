import pygame as pg
import tilesmanger

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

def gen_cells():
    for col in range(max_w):
        x = margin + col * (tile_heigth + margin)
        cells.append([])
        for row in range(max_h):
            y = margin + row * (tile_width + margin)
            rect = pg.Rect(x, y, tile_width, tile_heigth)
            pg.draw.rect(win, BLACK, rect)
            y += tile_heigth + margin
            cells[col].append(rect)
        x += tile_width + margin

def main():
    gen_cells()
    running = True
    while running:
        for e in pg.event.get(): 
            if e.type == pg.QUIT: # check for exit
                running = False
        if e.type == pg.MOUSEBUTTONUP and e.button == 1: # on mouse click
            x,y = e.pos
            for row in cells:
                for rect in row:
                    if rect.collidepoint(x,y):
                        pg.draw.rect(win, WHITE, rect)
        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()