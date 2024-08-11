import turtle
import pandas
screen =turtle.Screen()
screen.title("U.S . States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data =pandas.read_csv("50_states.csv")
all_state = data["state"].tolist()
guessed_states = []





while len(guessed_states) < 50 :

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?")
    print(answer_state)

    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data =data[data.state== answer_state]
        #pull out the row
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

screen.exitonclick()
