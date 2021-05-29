import pandas
import turtle

FONT = ('Courier', 10, 'normal')


class Game:
    def __init__(self, path):
        self.data = pandas.read_csv(path)
        self.guessed_states = []
        self.correct = False
        self.exit = False
        self.title = ''
        self.state_list = []
        self.user_state_name = ''
        self.x_cor = 0
        self.y_cor = 0

    def start(self):
        self.state_list = self.data.state.to_list()

    def show_input(self):
        if len(self.guessed_states) > 0:
            return f'{len(self.guessed_states)}/{len(self.state_list)} States Correct'
        else:
            return "Guess the state"

    def check_answer(self, user_input):
        if user_input in self.state_list:
            self.correct = True
            self.user_state_name = user_input
            coordinates = self.data[self.data["state"] == f"{user_input}"]
            self.x_cor = int(coordinates['x'])
            self.y_cor = int(coordinates['y'])
            self.guessed_states.append(user_input)
            self.state_list.remove(user_input)

        elif user_input == 'Exit':
            self.exit = True
            df = pandas.DataFrame(self.state_list)
            df.to_csv("./unsolved_states.csv")
        else:
            self.correct = False

    def draw_state_name(self):
        pen = turtle.Turtle()
        pen.penup()
        pen.hideturtle()
        pen.goto(x=self.x_cor, y=self.y_cor)
        pen.write(f'{self.user_state_name}', font=FONT)

