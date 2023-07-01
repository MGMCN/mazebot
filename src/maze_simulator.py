import random


class Maze:
    def __init__(self, row=5, column=5, wall=1, trap=1):
        self.row = row
        self.column = column
        self.wall = wall
        self.trap = trap
        self.rewards = {'r': 0,
                        'w': 0,
                        't': -1,
                        's': 0,
                        'e': 1}
        self.actions = ['up', 'down', 'left', 'right']
        self.maze = [['r' for _ in range(column)] for _ in range(row)]
        self.state = [0, 0]

    def reset(self):
        self.state = [0, 0]

    def set_maze(self, tag, count):
        for temp in range(count):
            i = 0
            j = 0
            while self.maze[i][j] != 'r':
                i = random.randint(0, self.row - 1)
                j = random.randint(0, self.column - 1)
            self.maze[i][j] = tag

    def get_maze(self):
        self.maze[0][0] = 's'
        self.maze[self.row - 1][self.column - 1] = 'e'
        self.set_maze('w', self.wall)
        self.set_maze('t', self.trap)
        return self.maze

    def get_state(self):
        return self.state.copy()

    def get_actions(self):
        return self.actions

    def step(self, action):
        temp_state = self.state.copy()
        i = self.state[0]
        j = self.state[1]
        done = False
        if action == 'up':
            if i - 1 >= 0:
                temp_state[0] = i - 1
        elif action == 'down':
            if i + 1 <= self.row - 1:
                temp_state[0] = i + 1
        elif action == 'left':
            if j - 1 >= 0:
                temp_state[1] = j - 1
        elif action == 'right':
            if j + 1 <= self.column - 1:
                temp_state[1] = j + 1

        if self.maze[temp_state[0]][temp_state[1]] != 'w':
            self.state = temp_state.copy()

        if self.maze[temp_state[0]][temp_state[1]] == 'e' or self.maze[temp_state[0]][temp_state[1]] == 't':
            done = True

        return self.state.copy(), self.rewards[self.maze[self.state[0]][self.state[1]]], done
