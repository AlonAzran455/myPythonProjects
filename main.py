import turtle
import pygame
import time
pygame.mixer.init()


def play_correct_sound():
    pygame.mixer.music.load("correct.mp3")
    pygame.mixer.music.play()


def play_incorrect_sound():
    pygame.mixer.music.load("incorrect.mp3")
    pygame.mixer.music.play()

def showGif(screen):
    screen.register_shape("myimage.gif")
    image_turtle = turtle.Turtle()
    image_turtle.shape("myimage.gif")
    image_turtle.penup()

    for x in range(-300, 300):
        image_turtle.goto(x, -50)
        time.sleep(0.0005)
        screen.update()
    image_turtle.hideturtle()


def display_question(t, question):
    t.clear()
    t.goto(0, 100)
    t.write("Solve for X:", align="center", font=("Arial", 20, "bold"))
    t.goto(0, 50)
    t.write(question, align="center", font=("Arial", 18, "normal"))


def show_intro_image(screen):
    screen.bgcolor("white")
    screen.register_shape("alons math project intro.gif")
    intro = turtle.Turtle()
    intro.shape("alons math project intro.gif")
    intro.penup()
    intro.goto(0, 0)
    screen.update()
    time.sleep(3)
    intro.hideturtle()

def is_valid_number(text):
    try:
        float(text)
        return True
    except (ValueError, TypeError):
        return False

def main():
    screen = turtle.Screen()
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.attributes('-fullscreen', True)
    screen.title("Math Quiz")
    screen.bgcolor("white")
    screen.setup(width=800, height=600)
    screen.tracer(0)  # Disable auto screen updates
    show_intro_image(screen)
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
                continue  # user clicked cancel or closed input
            if not is_valid_number(ans):
                continue
            if float(ans) == float(answers[i]):
                correct = True
                play_correct_sound()
                showGif(screen)
            else:
                writer.goto(0, -100)
                play_incorrect_sound()
                time.sleep(1)
                screen.update()

    writer.clear()
    writer.goto(0, 0)
    writer.write("Congratulations! You've completed the quiz.", align="center", font=("Arial", 20, "bold"))
    screen.update()
    screen.mainloop()


main()
