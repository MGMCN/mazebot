import tkinter as tk


class MazeView(tk.Tk):
    def __init__(self, mz):
        super(MazeView, self).__init__()
        self.start = None
        self.cv = None
        self.maze = mz
        self.wm_title("mazeBot")
        self.geometry('{0}x{1}'.format(len(self.maze) * 36 + 5, len(self.maze[0]) * 36 + 5))
        self.tags = {'r': "gray",
                     'w': "saddlebrown",
                     't': "black",
                     's': "red",
                     'e': "green"}
        self.build_maze()

    def build_maze(self):
        self.cv = tk.Canvas(self, bg="white", width=len(self.maze) * 36 + 5, height=len(self.maze[0]) * 36 + 5)
        i = 0
        for row in self.maze:
            j = 0
            for each_column in row:
                self.cv.create_rectangle(j, i, j + 36, i + 36, fill=self.tags[each_column])
                j += 36
            i += 36
        self.cv.pack()

    def reset(self):
        if self.start is None:
            self.start = self.cv.create_oval(8, 8, 28, 28, fill="yellow")
        else:
            self.render(0, 0)

    def render(self, x, y):
        x *= 36
        y *= 36
        x += 8
        y += 8
        self.cv.coords(self.start, y, x, y + 20, x + 20)
        self.update()
