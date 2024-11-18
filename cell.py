from graphics import Line, Point

class Cell:
    def __init__(self, window=None):
        self._win = window
        
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.visited = False
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.cell_visited = False
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            left_wall_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall_line,"black")
        else:
            left_wall_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall_line,"white")

        if self.has_right_wall:
            right_wall_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall_line,"black")
        else:
            right_wall_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall_line,"white")

        if self.has_top_wall:
            top_wall_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall_line,"black")
        else:
            top_wall_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall_line,"white")

        if self.has_bottom_wall:
            bottom_wall_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall_line,"black")
        else:
            bottom_wall_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall_line,"white")

    def draw_move(self, to_cell, undo=False):
        fill_color = 'red'
        if undo:
            fill_color = 'grey'
            
        first_cell_midpoint  = ((self._x1+self._x2)/2, (self._y1+self._y2)/2)
        second_cell_midpoint = ((to_cell._x1+to_cell._x2)/2, (to_cell._y1+to_cell._y2)/2)
        cell_to_cell_line = Line(Point(first_cell_midpoint[0], first_cell_midpoint[1]), Point(second_cell_midpoint[0], second_cell_midpoint[1]))
        self._win.draw_line(cell_to_cell_line, fill_color)



