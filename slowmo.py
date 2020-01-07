import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import imutils
from tkinter import *
w = 666
h = 400

window = tkinter.Tk()
window.title("OUT OR NOT")
img = cv2.cvtColor(cv2.imread("new.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=w, height=h)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
can_img = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()


#Functions

stream = cv2.VideoCapture("dhoni.avi")

def play(speed):

    print(f"speed is {speed}")

    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=666, height=400)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def out():
    print("OUT!!!")

def notout():
    print("NOTOUT!!!")


#BUTTONS



User_Input = Entry(window)



btn = tkinter.Button(window, text="Update", width=50)
btn.pack()

btn = tkinter.Button(window, text="<< FAST Backward", width=50, command=partial(play, -50))
btn.pack()

btn = tkinter.Button(window, text="<< Backward", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Forward >>", width=50, command=partial(play, 0.5))
btn.pack()

btn = tkinter.Button(window, text="FAST Forward >>", width=50, command=partial(play,100))
btn.pack()

btn = tkinter.Button(window, text="NOTOUT", width=50, command=notout)
btn.pack()

btn = tkinter.Button(window, text="OUT", width=50, command=out)
btn.pack()



window.mainloop()
