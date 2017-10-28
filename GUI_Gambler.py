from tkinter import *
from AnimatedGif import *
from tkinter.font import Font
from random import randint
from tkinter import messagebox
import time
from threading import Timer
import os
import PIL.Image
import pyglet
import pdb

root = Tk()

root.title("GUI Gambler")
root.geometry("450x400")

lines = "-" * 69

def diceplayer():
	#pdb.set_trace()
	wager = open("Wager.txt", "r").read()
	guessednumber = open("GuessedNumber.txt", "r").read()
	rangechoice = open("RangeChoice.txt", "r").read()
	balance = open("Balance.txt", "r").read()
	number = open("Number.txt", "r").read()
	if guessednumber == number:
		realpayback = int(wager) * int(rangechoice)
		messagebox.showinfo("Correct!", " You Win " + str(realpayback) + " Dollars!")
		balance = int(balance) + realpayback
		open("Balance.txt", "w").close()
		saveFile = open("Balance.txt", "w")
		saveFile.write(str(balance))
		saveFile.close()
		saveFile = open("StartOrNot.txt", "w")
		saveFile.write("NO")
		saveFile.close()
		open("Wager.txt", "w").close()
		open("GuessedNumber.txt", "w").close()
		open("RangeChoice.txt", "w").close()
		open("Number.txt", "w").close()
		label.place(x = "270", y = "0")
		balance = open("Balance.txt", "r").read()
		label2.place(x = "0", y = "255")
		title.place(x = "0", y = "0")
		lineslabel.place(x = "0", y = "50")
		step1.place(x = "0", y = "70")
		step2.place(x = "250", y = "155")
		b1.place(x = "0", y = "95")	
		b2.place(x = "0", y = "125")
		b3.place(x = "0", y = "155")
		step2infolabel = Label(root, text="Place Your Wager In-Between 10 And " + str(balance))
		step2infolabel.place(x = "190", y = "175")
		wagerentry.place(x = "250", y = "195")
		step3.place(x = "250", y = "235")
		guessednumberentry.place(x = "250", y = "255")
		submit.place(x = "295", y = "300")
		balancelabel = Label(root, text = "Balance: " + str(balance))
		balancelabel.configure(font=my2ndFont)
		balancelabel.destroy()
		balancelabel = Label(root, text = "Balance: " + str(balance))
		balancelabel.configure(font=my2ndFont)
		balancelabel.place(x = "150", y = "350")
		image3 = tk.PhotoImage(file="0.png")
		image4 = tk.PhotoImage(file="1.png")
		image5 = tk.PhotoImage(file="2.png")
		image6 = tk.PhotoImage(file="3.png")
		image7 = tk.PhotoImage(file="4.png")
		image8 = tk.PhotoImage(file="5.png")
		label81 = tk.Label(image=image3)
		label81.image = image3
		label9 = tk.Label(image=image4)
		label9.image = image4
		label10 = tk.Label(image=image5)
		label10.image = image5
		label11 = tk.Label(image=image6)
		label11.image = image6
		label12 = tk.Label(image=image7)
		label12.image = image7
		label13 = tk.Label(image=image8)
		label13.image = image8
	else:
		messagebox.showinfo("Wrong!", "Incorrect!  You Lose " + str(wager) + " Dollars!\nYou Guessed " + str(guessednumber) + "!\nThe Real Number Was " + number)
		balance = int(balance) - int(wager)
		open("Balance.txt", "w").close()
		saveFile = open("Balance.txt", "w")
		saveFile.write(str(balance))
		saveFile.close()
		saveFile = open("StartOrNot.txt", "w")
		saveFile.write("NO")
		saveFile.close()
		open("Wager.txt", "w").close()
		open("GuessedNumber.txt", "w").close()
		open("RangeChoice.txt", "w").close()
		open("Number.txt", "w").close()
		step2infolabel = Label(root, text="Place Your Wager In-Between 10 And " + str(balance))
		label.place(x = "270", y = "0")
		label2.place(x = "0", y = "255")
		title.place(x = "0", y = "0")
		lineslabel.place(x = "0", y = "50")
		step1.place(x = "0", y = "70")
		step2.place(x = "250", y = "155")
		b1.place(x = "0", y = "95")	
		b2.place(x = "0", y = "125")
		b3.place(x = "0", y = "155")
		step2infolabel.place(x = "190", y = "175")
		wagerentry.place(x = "250", y = "195")
		step3.place(x = "250", y = "235")
		guessednumberentry.place(x = "250", y = "255")
		submit.place(x = "295", y = "300")
		balancelabel = Label(root, text = "Balance: " + str(balance))
		balancelabel.destroy()
		balancelabel = Label(root, text = "Balance: " + str(balance))
		balancelabel.configure(font=my2ndFont)
		#balancelabel.place_forget()
		balancelabel.place(x = "150", y = "350")
		image3 = tk.PhotoImage(file="0.png")
		image4 = tk.PhotoImage(file="1.png")
		image5 = tk.PhotoImage(file="2.png")
		image6 = tk.PhotoImage(file="3.png")
		image7 = tk.PhotoImage(file="4.png")
		image8 = tk.PhotoImage(file="5.png")
		label81 = tk.Label(image=image3)
		label81.image = image3
		label9 = tk.Label(image=image4)
		label9.image = image4
		label10 = tk.Label(image=image5)
		label10.image = image5
		label11 = tk.Label(image=image6)
		label11.image = image6
		label12 = tk.Label(image=image7)
		label12.image = image7
		label13 = tk.Label(image=image8)

def endanimation():
	label13.place_forget()
	#balancelabel.place_forget()
	rangesystem()

def place6():
	label12.place_forget()
	t7 = Timer(0.1, endanimation)
	t7.start()
	label13.place(x = "90", y = "50")

def place5():
	label11.place_forget()
	t6 = Timer(0.1, place6)
	t6.start()
	label12.place(x = "90", y = "50")

def place4():
	label10.place_forget()
	t5 = Timer(0.1, place5)
	t5.start()
	label11.place(x = "90", y = "50")

def place3():
	label9.place_forget()
	t4 = Timer(0.1, place4)
	t4.start()
	label10.place(x = "90", y = "50")

def place2():
	label81.place_forget()
	step2infolabel.place_forget()
	t3 = Timer(0.1, place3)
	t3.start()
	label9.place(x = "90", y = "50")


def rangesystem():
	rangechoice = open("RangeChoice.txt", "r").read()
	if int(rangechoice) == 1:
		#number = randint(1,10)
		number = 3
		saveFile = open("Number.txt", "w")
		saveFile.write(str(number))
		saveFile.close()
		balancelabel.destroy()
		##balancelabel.place_forget()
		step2infolabel.place_forget()
		diceplayer()
	elif int(rangechoice) == 2:
		number = randint(1,50)
		saveFile = open("Number.txt", "w")
		saveFile.write(str(number))
		saveFile.close()
		#balancelabel.place_forget()
		step2infolabel.place_forget()
		diceplayer()
	elif int(rangechoice) == 3:
		number = randint(1,100)
		saveFile = open("Number.txt", "w")
		saveFile.write(str(number))
		saveFile.close()
		#balancelabel.place_forget()
		step2infolabel.place_forget()
		diceplayer()
	else:
		print("Error")

def delete():
	root.destroy()

def wagerthemoney(wager, guessednumber, rangechoice, balance):
	try:
		int(wager)
	except ValueError:
		messagebox.showinfo("Invalid", "Put In A Valid Number!")
	try:
		int(guessednumber)
	except ValueError:
		messagebox.showinfo("Invalid", "Put In A Valid Number!")

	if int(wager) > int(balance):
		messagebox.showinfo("Sorry!","You Don't Have That Kind Of Cash!  Try Again!")
	elif int(wager) < 10:
		messagebox.showinfo("Cheapo", "Come On Man!  Bet At Least 10!")
	elif int(wager) >= 10 & int(wager) <= int(balance):
		if guessednumber == "":
			messagebox.showinfo("Unsuccesful!", "Try Again!")
		else:
			messagebox.showinfo("Succesful!", "Wager Accepted!") 
			saveFile = open("Wager.txt", "w")
			saveFile.write(wager)
			saveFile.close()
			saveFile = open("GuessedNumber.txt", "w")
			saveFile.write(guessednumber)
			saveFile.close()
			saveFile = open("RangeChoice.txt", "w")
			saveFile.write(str(rangechoice))
			saveFile.close()
			label.place_forget()
			label2.place_forget()
			title.place_forget()
			lineslabel.place_forget()
			step1.place_forget()
			step2.place_forget()
			b1.place_forget()
			b2.place_forget()
			b3.place_forget()
			step2infolabel.place_forget()
			wagerentry.place_forget()
			step3.place_forget()
			guessednumberentry.place_forget()
			submit.place_forget()
			##balancelabel.place_forget()
			t2 = Timer(0.1, place2)
			t2.start()
			label81.place(x = "90", y = "50")
			step2infolabel.place_forget()
	else:	
		print("\nThat Is Not A Valid Wager!")

def getinfo():
	#balancelabel.place_forget()
	#balancelabel.destroy()
	balancelabel = Label(root, text = "")
	balancelabel.place_forget()
	rangechoice = rbVar.get()
	wager = wagerentry.get()
	guessednumber = guessednumberentry.get()
	balance = open("Balance.txt", "r").read()
	wagerthemoney(wager, guessednumber, rangechoice, balance)


balance = open("Balance.txt", "r").read()
image = tk.PhotoImage(file="Dice.png")
image2 = tk.PhotoImage(file="Dice.png")
myFont = Font(family="Comic Sans MS", size=25)
my2ndFont = Font(family = "Comic Sans MS", size = 20)

label = tk.Label(image=image)
label2 = tk.Label(image=image2)
title = Label(root, text = "GUI Dice Gambler")
title.configure(font=myFont)
lineslabel = Label(root, text = lines)


rbVar = IntVar()
b1 = Radiobutton(root, text="1-10 (1x Your Wager)", value=1, variable = rbVar)
b2 = Radiobutton(root, text="1-50 (2x Your Wager)", value=2, variable = rbVar)
b3 = Radiobutton(root, text="1-100 (3x Your Wager)", value=3, variable = rbVar)
step1 = Label(root, text="Step 1: Choose Your Range")
step2 = Label(root, text="Step 2: Place Your Wager")
step3 = Label(root, text="Step 3: Guess The Number")
step2infolabel = Label(root, text="Place Your Wager In-Between 10 And " + str(balance))
wagerentry = Entry(root)
guessednumberentry = Entry(root)
submit = Button(root, text = "Submit", command = getinfo)
balancelabel = Label(root, text = "Balance: " + str(balance))
balancelabel.configure(font=my2ndFont)
image3 = tk.PhotoImage(file="0.png")
image4 = tk.PhotoImage(file="1.png")
image5 = tk.PhotoImage(file="2.png")
image6 = tk.PhotoImage(file="3.png")
image7 = tk.PhotoImage(file="4.png")
image8 = tk.PhotoImage(file="5.png")
label81 = tk.Label(image=image3)
label81.image = image3
label9 = tk.Label(image=image4)
label9.image = image4
label10 = tk.Label(image=image5)
label10.image = image5
label11 = tk.Label(image=image6)
label11.image = image6
label12 = tk.Label(image=image7)
label12.image = image7
label13 = tk.Label(image=image8)
label13.image = image8

rangechoice = rbVar.get()

label.place(x = "270", y = "0")
label2.place(x = "0", y = "255")
title.place(x = "0", y = "0")
lineslabel.place(x = "0", y = "50")
step1.place(x = "0", y = "70")
step2.place(x = "250", y = "155")
b1.place(x = "0", y = "95")	
b2.place(x = "0", y = "125")
b3.place(x = "0", y = "155")
step2infolabel.place(x = "190", y = "175")
wagerentry.place(x = "250", y = "195")
step3.place(x = "250", y = "235")
guessednumberentry.place(x = "250", y = "255")
submit.place(x = "295", y = "300")
balancelabel.place(x = "150", y = "350")

root.mainloop()