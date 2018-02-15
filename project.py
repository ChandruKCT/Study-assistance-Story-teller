from PIL import ImageTk,Image 
import pytesseract 
import PIL.Image

from tkinter import *
import tkinter
from tkinter import filedialog, font
import time
import subprocess
from espeak import espeak
import os
#from textract import process


master = Tk()
master.geometry("1000x1000")
master.wm_title("Tale reader")

master.configure(background="#fff")

PILFile = PIL.Image.open("listen.jpg").convert("RGB")
Image = ImageTk.PhotoImage(PILFile) # <---
ImageLabel = Label(master, image=Image)
ImageLabel.image = Image
ImageLabel.pack()


w = Label(master, text="Study assistant")
w.config(width=20, height = 2)
w.configure(background="#fff")
w.config(font=("Times", 33))
w.config(highlightbackground='black')
w.pack()


def imageVoice():
	def again():
		espeak.synth(x)
		# try:
		# 	print ("Hi")
		# 	os.system("echo " + x + " | espeak -v female3 -s 120")   --> feamle voice
		# except:
		# 	espeak.synth(x)   ---> male voice 

	file_path = filedialog.askopenfilename()
	a = PIL.Image.open(file_path).convert("RGB")
	x = pytesseract.image_to_string(a)
	x = x.replace("\n", " ")
	print (x)
	try:
		espeak.synth(x)
		#os.system("echo " + x + " | espeak -v female3 -s 120")
	except:
		espeak.synth(x)
	replay = Button(master, text="replay image", command=again)
	replay.config(width=12, height = 1)
	replay.configure(background="#fff")
	replay.config(font=("Courier", 10))
	replay.pack()

def textVoice():
	global voo
	def ok():
		espeak.synth(e1.get())
		#os.system("echo " + e1.get() + " | espeak -v female3")
	if voo == 1:
		voo = 2
		e1 = Entry(master, width=25)
		e1.pack()
		b = Button(master, text="Convert audio", command=ok)
		b.config(width=15, height = 1)
		b.configure(background="#fff")
		b.config(font=("Courier", 10))
		b.pack()

def pdfVoice():
	global vee
	def again():
		espeak.synth(text)
	file_path = filedialog.askopenfilename()
	text = process(file_path)
	text = text.decode("utf-8")
	print (text)
	espeak.synth(text)
	if vee == 1:
		vee = 2
		replay = Button(master, text="replay pdf", command=again)
		replay.config(width=12, height = 1)
		replay.configure(background="#fff")
		replay.config(font=("Courier", 10))
		replay.pack()


b = Button(master, text="Choose file", command=imageVoice)
b.config(width=10, height = 1)
b.configure(background="#fff")
b.config(font=("Courier", 22))
b.pack()

voo = 1
c = Button(master, text="Enter text", command=textVoice)
c.config(width=10, height = 1)
c.configure(background="#fff")
c.config(font=("Courier", 22))
c.pack()

vee = 1
pd = Button(master, text="Select pdf", command=pdfVoice)
pd.config(width=10, height = 1)
pd.configure(background="#fff")
pd.config(font=("Courier", 22))
pd.pack()

mainloop()