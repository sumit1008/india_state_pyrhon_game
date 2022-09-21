import turtle
import pandas as pd

screen =turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

screen.title("india states game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

answer_state=screen.textinput(title="Guess the state",prompt="what's another state name?").title()
# print(answer_state)

data=pd.read_csv("states2.csv")
game=turtle.Turtle()
game.penup()
game_over=True
count=0
while game_over:
    for i in range(36):
        if answer_state==data["STATE"][i]:
            print(f"matched{i}")
            
            game.setposition(data["x"][i],data["y"][i])
            game.write(data["STATE"][i])
            print(data["x"][i])
            count+=1
            answer_state=screen.textinput(title=f"{count}/36 correct in states and UT's",prompt="what's another state name?").title()
        else:
            
            game_over=False

game.setposition(170,350)
game.write("there is no state like this you lost") 
print(answer_state)


# print(data["STATE"][0])
# no_of_states=len(pd.DataFrame(data))
# print(no_of_states)

turtle.mainloop()

















# def get_cordinate(x,y):
#     print(x,y)

# turtle.onscreenclick(get_cordinate)
# turtle.mainloop()

