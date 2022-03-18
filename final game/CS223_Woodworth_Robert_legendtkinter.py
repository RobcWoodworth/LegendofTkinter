#!/usr/bin/env python3
# Rob Woodworth CS223 Hangman 2/22/22
from tkinter import *
from tkinter import messagebox
import time
root = Tk()
root.title("The Legend of Tkinter")
root.geometry("800x500")
root['background'] = '#000'
lbl_word, lbl_life = Label(root, text=""), Label(root, text="")
lives, splash, lbl_q = 8, PhotoImage(file="splash.gif"), Label(root, text="")
game, dead = PhotoImage(file="game.gif"), PhotoImage(file="dead.gif")
talking, hurts = PhotoImage(file="talking.gif"), PhotoImage(file="hurt.gif")
wins1, wins2 = PhotoImage(file="win1.gif"), PhotoImage(file="win2.gif")
Label(root, text="Bobbo's Grocery presents", font=("Terminal", 25),
      bg="#000", fg="#FFF", ).place(x=120, y=190)


def splash_screen():  # creating an intro animation with time sleep
    global lbl_word
    root.update()
    screen = Label(root, image=splash)
    screen.place(x=0, y=0)
    time.sleep(1.5)
    root.update()
    lbl_word = Label(root, text="TKINTER", font=("Terminal", 85), bg="#fba110")
    lbl_word.place(x=180, y=110)
    time.sleep(1.5)
    root.update()
    Button(root, width=19, text="PUSH START BUTTON", font=("Terminal", 25),
           command=intro, bg="#fcd2b3").place(x=170, y=410)
    time.sleep(1.5)
    root.update()


def intro():  # This is the first intro screen
    global lbl_word
    screen = Label(root, image=talking)
    screen.place(x=0, y=0)
    lbl_word = Label(root, text="Hey it's me,\nJohn Family Guy!\n\n"
                                "I can't wait to get home\nhere in the"
                                " beautiful\nland of Hyrule",
                     font=("Terminal", 22), bg="#f5d89e")
    lbl_word.place(x=310, y=110)
    Button(root, width=12, text="Okay!", font=("Terminal", 25),
           command=intro2, bg="#72ff69").place(x=400, y=350)


def intro2():  # This is the second intro screen
    global lbl_word
    lbl_word["text"] = "It's just me and my\ngood pal, the button."\
                       "\n\nHe just loves getting\nclicked on,"\
                       " don't ya?\n\nHey! HEY!! NO! BAD!"
    Button(root, width=12, text="Grrrr!", font=("Terminal", 25),
           command=intro3, bg="#f00").place(x=400, y=350)


def intro3():  # This is the third intro screen.
    global lbl_word
    lbl_word["text"] = "I know what we need here!\n\n" \
                       "I'll beat you with the power\n" \
                       "of a Python trivia quiz!"
    Button(root, width=12, text="Uh... Grrr?", font=("Terminal", 25),
           command=question1, bg="#f00").place(x=400, y=350)


def question1():  # The start of the game
    global lives, lbl_life, lbl_q
    screen, lives = Label(root, image=game), 7
    screen.place(x=0, y=0)
    lbl_life = Label(root, text="♥" * lives, font=("Terminal", 30),
                     bg="#000", fg="#f00")
    lbl_life.place(x=520, y=70)
    lbl_q = Label(root, text="1: Which of these operators can NOT be used"
                             " on strings?", font=("Terminal", 15),
                  bg="#000", fg="#fff")
    lbl_q.place(x=100, y=120)
    Button(root, width=6, text="MAIN\nMENU", font=("Arial", 12),
           command=splash_screen, fg='#fff', bg="red").place(x=10, y=10)
    Button(root, width=8, text="+", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=110, y=250)
    Button(root, width=8, text="*", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=260, y=250)
    Button(root, width=8, text="in", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=410, y=250)
    Button(root, width=8, text="-", font=("Terminal", 20),
           command=question2, bg="#fff").place(x=560, y=250)


def question2():  # This is the second question
    messagebox.showinfo("Correct!", "Strings cannot be subtracted")
    global lives, lbl_q
    lbl_q["text"] = "2: What is 1 / 1 ?"
    Button(root, width=6, text="MAIN\nMENU", font=("Arial", 12),
           command=splash_screen, fg='#fff', bg="red").place(x=10, y=10)
    Button(root, width=8, text="1", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=110, y=250)
    Button(root, width=8, text="1.0", font=("Terminal", 20),
           command=question3, bg="#fff").place(x=260, y=250)
    Button(root, width=8, text="\"1\"", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=410, y=250)
    Button(root, width=8, text="[1]", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=560, y=250)


def question3():  # This is the third question
    messagebox.showinfo("Correct", "Dividing integers always produces a float")
    global lives, lbl_q, lbl_life               # had to reload the BG to cover
    Label(root, image=game).place(x=0, y=0)            # up the smaller buttons
    lbl_life = Label(root, text="♥" * lives, font=("Terminal", 30),
                     bg="#000", fg="#f00")
    lbl_life.place(x=520, y=70)
    lbl_q = Label(root, text="3: How do you find the length of a string named "
                             "str?", font=("Terminal", 15),
                  bg="#000", fg="#fff")
    lbl_q.place(x=100, y=120)
    Button(root, width=6, text="MAIN\nMENU", font=("Arial", 12),
           command=splash_screen, fg='#fff', bg="red").place(x=10, y=10)
    Button(root, width=12, text="str._len_()", font=("Terminal", 15),
           command=hurt, bg="#fff").place(x=110, y=250)
    Button(root, width=12, text="len(str)", font=("Terminal", 15),
           command=question4, bg="#fff").place(x=260, y=250)
    Button(root, width=12, text="str.size()", font=("Terminal", 15),
           command=hurt, bg="#fff").place(x=410, y=250)
    Button(root, width=12, text="size(str)", font=("Terminal", 15),
           command=hurt, bg="#fff").place(x=560, y=250)


def question4():  # This is the fourth question
    messagebox.showinfo("Correct", "len(str) is the correct syntax")
    global lives, lbl_life, lbl_q
    lbl_q["text"] = "4: What is '24' * 3?"
    Button(root, width=6, text="MAIN\nMENU", font=("Arial", 12),
           command=splash_screen, fg='#fff', bg="red").place(x=10, y=10)
    Button(root, width=8, text="'242424'", font=("Terminal", 20),
           command=question5, bg="#fff").place(x=110, y=250)
    Button(root, width=8, text="72", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=260, y=250)
    Button(root, width=8, text="'24', 3", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=410, y=250)
    Button(root, width=8, text="(error)", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=560, y=250)


def question5():  # This is the fifth question
    messagebox.showinfo("Correct!", "Multiplying a string concatenates it")
    global lives, lbl_life, lbl_q
    lbl_q["text"] = "5: What will print(len([None, None, None, 1])) output?"
    Button(root, width=6, text="MAIN\nMENU", font=("Arial", 12),
           command=splash_screen, fg='#fff', bg="red").place(x=10, y=10)
    Button(root, width=8, text="0", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=110, y=250)
    Button(root, width=8, text="1", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=260, y=250)
    Button(root, width=8, text="(error)", font=("Terminal", 20),
           command=hurt, bg="#fff").place(x=410, y=250)
    Button(root, width=8, text="4", font=("Terminal", 20),
           command=win1, bg="#fff").place(x=560, y=250)


def hurt():  # wrong answers point here, removes a life and checks if dead
    screen = Label(root, image=hurts)
    screen.place(x=0, y=0)
    root.update()
    time.sleep(.4)
    screen.place(x=1000, y=1000)
    root.update()
    global lbl_life, lives
    lives -= 1
    lbl_life["text"] = "♥" * lives
    if lives <= 0:  # displays dead screen and restart button
        screen = Label(root, image=dead)
        screen.place(x=0, y=0)
        Button(root, width=6, text="MAIN\nMENU", font=("Arial", 12),
               command=splash_screen, fg='#fff', bg="red").place(x=380, y=300)
    pass


def win1():  # the first winning screen
    messagebox.showinfo("Correct!", "len still counts None as a list item")
    screen = Label(root, image=wins1)
    screen.place(x=0, y=0)
    Button(root, width=12, text="Okay!", font=("Terminal", 25),
           command=win2, bg="#72ff69").place(x=400, y=350)


def win2():  # The final winning screen and happy ending
    screen = Label(root, image=wins2)
    screen.place(x=0, y=0)
    Button(root, width=6, text="MAIN\nMENU", font=("Arial", 12),
           command=splash_screen, fg='#fff', bg="red").place(x=520, y=350)


splash_screen()
root.mainloop()
