# with OOP
import turtle
import game

my_screen = turtle.Screen()
my_screen.title("U.S. States Game")
image = "./blank_states_img.gif"
my_screen.addshape(image)
my_screen.setup(width=725, height=491)
turtle.shape(image)

my_game = game.Game('./50_states.csv')
my_game.start()

while len(my_game.guessed_states) != 50 and not my_game.exit:
    user_input = my_screen.textinput(title=my_game.show_input(), prompt="What's another state name?").title()
    my_game.check_answer(user_input)
    if my_game.correct:
        my_game.draw_state_name()



