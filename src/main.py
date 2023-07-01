import time
from maze_simulator import Maze
from qlearning import QLearningTable
from maze_view import MazeView


def play():
    while True:
        maze.reset()
        view.reset()

        state = maze.get_state()
        while True:
            action = bot.choose_action(str(state))
            next_state, reward, done = maze.step(action)

            bot.learning(str(state), action, reward, str(next_state), done)

            state = next_state
            time.sleep(0.05)
            view.render(state[0], state[1])

            if done:
                break

        if reward > 0 and done is True:
            bot.increase_epsilon()


if __name__ == "__main__":
    maze = Maze(wall=2, trap=2)
    maze_map = maze.get_maze()

    e_greedy_increment = 0.01
    bot = QLearningTable(maze.get_actions(), e_greedy=0.5, e_greedy_increment=e_greedy_increment)

    view = MazeView(maze_map)
    view.after(1, play)
    view.mainloop()
