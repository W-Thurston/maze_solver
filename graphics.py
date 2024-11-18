from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver") 
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running_flag = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running_flag = True
        while self.__running_flag:
            self.redraw()
        print("window closed...")
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running_flag = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.point_1.x, self.point_1.y,
                           self.point_2.x, self.point_2.y,
                           fill = fill_color, width=2)