import pyqrcode
import png
from pyqrcode import QRCode
import tkinter as tk
from tkinter import *

'''
Tkinter Module – helps to create the GUI window for the project.
Png Module – This helps to save an image in the png extension.
Pyqrcode Module – This Module helps to generate a QR Code.
'''
#---Create a window
window = Tk()

window.geometry('400x450')

window.title('PythonGeeks')

Label(window, text="Let's make a qr code!", font='arial 15').pack()


#---Create a window

s = StringVar()

def create_qrcode():
    s1=s.get()
    qr = pyqrcode.create(s1)
    qr.png('myqr.png', scale = 6)
    Label(window,text='QR Code is created and saved.').pack()