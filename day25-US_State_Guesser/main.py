import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Guesser")

image = "day25-US_State_Guesser/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("day25-US_State_Guesser/data/50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? 'Exit' to quit.",
    ).title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        # print(state_data)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(state_data.iloc[0].x), int(state_data.iloc[0].y))
        t.write(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame({"missing_states": missing_states})
        new_data.to_csv("day25-US_State_Guesser/data/missing_states.csv")
        break


screen.exitonclick()
