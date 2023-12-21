from enum import Enum
import pygame as pg

Direction = Enum("Direction",["UP", "DOWN", "LEFT", "RIGHT", "NONE"])

YELLOW = (237,219,90)
BLACK = (0,0,0)

class tilesmanger:
    def __init__(self, win: pg.Surface) -> None:
        self.win = win
        # self.tilemap = [
        #     tile(Direction.UP),tile(Direction.DOWN),tile(Direction.RIGHT),tile(Direction.LEFT)
        # ]

class tile:
    def __init__(self, tm: tilesmanger, rect: pg.Rect, side: Direction = Direction.NONE) -> None:
        self.side = side
        self.rect = rect
        self.win = tm.win
        self.collider = None

    def handle_side(self):
        self.handle_none()
        if type(self.side) != tuple:
            self.render_side(self.side)
            return
        for side in self.side:
            self.render_side(side)
    
    def render_side(self, side):
        match side:
            case Direction.UP: self.handle_up()
            case Direction.DOWN: self.handle_down()
            case Direction.LEFT: self.handle_left()
            case Direction.RIGHT: self.handle_right()
            case Direction.NONE: self.handle_none()
            case _: raise ValueError("?!")
    
    def handle_none(self):
        self._set_colour(YELLOW)
    
    def handle_up(self):
        self.collider = pg.Rect(self.rect.left, self.rect.top, self.rect.width, 5)
        pg.draw.rect(self.win, BLACK, self.collider)

    def handle_down(self):
        self.collider = pg.Rect(self.rect.left, self.rect.bottom-5, self.rect.width, 5)
        pg.draw.rect(self.win, BLACK, self.collider)

    def handle_left(self):
        self.collider = pg.Rect(self.rect.left, self.rect.top, 5, self.rect.height)
        pg.draw.rect(self.win, BLACK, self.collider)
        print(f"{self.rect.left}, {self.rect.bottom}, 5,{self.rect.height}")

    def handle_right(self):
        self.collider = pg.Rect(self.rect.right-5, self.rect.top, 5, self.rect.height)
        pg.draw.rect(self.win, BLACK, self.collider)
        print(f"{self.rect.left}, {self.rect.bottom}, 5,{self.rect.height}")
    
    def _set_colour(self, colour):
        pg.draw.rect(self.win, colour, self.rect)
