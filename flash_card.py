from tkinter import *
from tkinter import PhotoImage
import random
import pandas
to_learn = {}
curr_card = {}

try:
    french_data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    french_data = pandas.read_csv("french_data.csv")
else:
    to_learn = french_data.to_dict(orient="records")

def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(to_learn)
    canvas.itemconfig(french, text="French", fill="red")
    canvas.itemconfig(fr_word, text=curr_card["French"], fill="black")
    canvas.itemconfig(card, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def learnt():
    to_learn.remove(curr_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(french, text="English", fill="red")
    canvas.itemconfig(fr_word, text=curr_card["English"], fill="white")
    canvas.itemconfig(card, image=card_back)

window = Tk()
window.title("Flash Card")
BACKGROUND_COLOR = "#B1DDC6"
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
french_data_dict = french_data.to_dict()
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
canvas = Canvas(width=800, height=526)
card = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0,column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_btn = Button(image=right_img, highlightthickness=0, bd=0, command=learnt)
wrong_btn = Button(image=wrong_img, highlightthickness=0, bd=0, command=next_card)
right_btn.grid(row=1, column=1)
wrong_btn.grid(row=1, column=0)
french = canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
fr_word = canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))
next_card()


window.mainloop()