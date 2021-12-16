# #100days of code - day 26 - US States Game

import turtle
import pandas
from publish import Publish

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []
no_states_user_guessed = 0
NO_OF_STATES = 50
game_is_on = True


while game_is_on:
    answer_state = str(screen.textinput(title=f"{no_states_user_guessed}/{NO_OF_STATES} Guess the State",
                                        prompt="What's another state's name?"))
    answer_state = answer_state.title()

    # print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if (answer_state in states_data.values) and (answer_state not in guessed_states):
        # print(states_data['x'], states_data["y"])
        x_pos = states_data[states_data.state == answer_state].x
        y_pos = states_data[states_data.state == answer_state].y
        Publish(answer_state, int(x_pos), int(y_pos))
        no_states_user_guessed += 1
        guessed_states.append(answer_state)
        if no_states_user_guessed == NO_OF_STATES:
            Publish("You guessed all states!", 0, 280)
            game_is_on = False


# screen.exitonclick()

# sprawdzanie pozycji myszki na ekranie i wyswietlanei wspolrzędnych
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
