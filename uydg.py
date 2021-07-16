from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("khiue")
root.geometry("600x400")

root.configure(background = "gold")

img=ImageTk.PhotoImage(Image.open("pokecard.jpg"))
img1=ImageTk.PhotoImage(Image.open("pokecard1.jpg"))
img2=ImageTk.PhotoImage(Image.open("pokecard2.jpg"))
img3=ImageTk.PhotoImage(Image.open("pokecard3.jpg"))
img4=ImageTk.PhotoImage(Image.open("pokecard4.jpg"))
img5=ImageTk.PhotoImage(Image.open("pokecard5.jpg"))
img6=ImageTk.PhotoImage(Image.open("pokecard6.jpg"))
img7=ImageTk.PhotoImage(Image.open("pokecard7.jpg"))
img8=ImageTk.PhotoImage(Image.open("pokecard8.jpg"))
img9=ImageTk.PhotoImage(Image.open("pokecard9.jpg"))
img0=ImageTk.PhotoImage(Image.open("pokecard0.jpg"))
img11=ImageTk.PhotoImage(Image.open("pokecard11.jpg"))

player1label = Label(root, text="Player 1", bg="cornflower blue",fg="white")
player1label.place(relx = 0.1,rely=0.3,anchor=CENTER)

player2label = Label(root, text="Player 2", bg="cornflower blue",fg="white")
player2label.place(relx = 0.9,rely=0.3,anchor=CENTER)

player1scorelabel = Label(root, text="Player 1 score : ", bg="cornflower blue",fg="white")
player1scorelabel.place(relx = 0.1,rely=0.4,anchor=CENTER)

player2scorelabel = Label(root, text="Player 1 score : ", bg="cornflower blue",fg="white")
player2scorelabel.place(relx = 0.9,rely=0.4,anchor=CENTER)

pokecardlabellabel = Label(root, bg="turquoise",fg="white")
pokecardlabellabel.place(relx = 0.5,rely=0.5,anchor=CENTER)

root.mainloop()