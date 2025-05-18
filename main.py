import turtle

def showGif():
    screen = turtle.Screen()
    screen.title("Good answer :)")
    screen.bgcolor("white")
    screen.setup(width=800, height=600)
    # Lift the window to the front using underlying Tkinter
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    screen.register_shape("d:\\myimage.gif")
    # Create a turtle and set the image as its shape
    image_turtle = turtle.Turtle()
    image_turtle.shape("d:\\myimage.gif")
    image_turtle.penup()  # Don't draw a line
    # Move the turtle in a loop to simulate motion
    for x in range(-300, 300, 5):
        image_turtle.goto(x, 0)
        screen.update()

    root.attributes('-topmost', False)
    root.lower()

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
    print(questions[i])
    ans = float(input("Answer the question, enter a number for X: "))
    while ans != float(answers[i]):
        ans = float(input("Wrong, try again. Enter a number for X: "))
    showGif()

