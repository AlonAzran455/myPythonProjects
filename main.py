import turtle


def showGif(screen):
    screen.register_shape("myimage.gif")
    image_turtle = turtle.Turtle()
    image_turtle.shape("myimage.gif")
    image_turtle.penup()

    for x in range(-300, 300):
        image_turtle.goto(x, 0)
        screen.update()
    image_turtle.hideturtle()

def display_question(t, question):
    t.clear()
    t.goto(0, 100)
    t.write("Solve for X:", align="center", font=("Arial", 20, "bold"))
    t.goto(0, 50)
    t.write(question, align="center", font=("Arial", 18, "normal"))

def main():
    screen = turtle.Screen()
    screen.title("Math Quiz")
    screen.bgcolor("white")
    screen.setup(width=800, height=600)
    screen.tracer(0)  # Disable auto screen updates

    # Turtle for showing questions
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()

    questions = [
        "2X + 9 = X + 1",
        "3X + 4 = X + 8",
        '9 - 7X = -3(2X - 3)',
        "0.8X + 1.2 = 40.8 - 3.6X",
        "-0.4 - 1.6X = 4X + 38.8",
        "0.8 - 2.8X = 0.8X - 28"
    ]

    answers = [-8, 2, 0, 9, -7, 8]

    for i in range(len(questions)):
        correct = False
        while not correct:
            display_question(writer, questions[i])
            screen.update()
            ans = screen.textinput("Your Answer", f"Enter a number for X in:\n{questions[i]}")
            if ans is None:
                return  # user clicked cancel or closed input
            try:
                if float(ans) == float(answers[i]):
                    correct = True
                    showGif(screen)
                else:
                    writer.goto(0, -100)
                    writer.write("Wrong! Try again.", align="center", font=("Arial", 16, "italic"))
                    screen.update()
            except ValueError:
                writer.goto(0, -100)
                writer.write("Please enter a valid number!", align="center", font=("Arial", 16, "italic"))
                screen.update()

    writer.clear()
    writer.goto(0, 0)
    writer.write("Congratulations! You've completed the quiz.", align="center", font=("Arial", 20, "bold"))
    screen.update()
    screen.mainloop()

main()
