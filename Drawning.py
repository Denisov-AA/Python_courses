from tkinter import *

WIDTH = 800
HEIGHT = 300

# Creating window
root = Tk()
root.title("a.denisov")

# Creating canvas
window = Canvas(root, width=WIDTH, height=HEIGHT)
window.pack()

# Writing disclaimer
window.create_text(400, 100, text="Disclaimer", justify=CENTER, font="Times 26")
window.create_text(400, 200, text="This is first-time drawing program\nrun it on your own risk.\nGood luck!",
                   justify=CENTER, font="Times 18")


class Ball:

    # Class constructor
    def __init__(self):
        self.shape = window.create_oval(0, 0, 30, 30, fill="yellow")
        self.speedx = 20
        self.speedy = 20
        self.active = True
        self.move_active()

    # Defining move vector
    def ball_update(self):
        window.move(self.shape, self.speedx, self.speedy)
        pos = window.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    # Infinite loop for animation
    def move_active(self):
        if self.active:
            self.ball_update()
            root.after(40, self.move_active)


# ball = Ball()


def start(Ball):
    ball: Ball = Ball()


# Writing disclaimer
window.create_text(400, 100, text="Disclaimer", justify=CENTER, font="Times 26")
window.create_text(400, 200, text="This is first-time drawing program\nrun it on your own risk.\nGood luck!",
                   justify=CENTER, font="Times 18")

# Creating "NEXT" button and starting drawing function
Next_button = Button(text="I'm not afraid!", width=15, height=5, bg="red")
Next_button.pack(side=BOTTOM)
Next_button.bind('<Button-1>', func=start)

root.mainloop()
