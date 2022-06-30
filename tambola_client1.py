import socket
from tkinter import *
from threading import Thread
import random
from PIL import ImageTk, Image

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    
    PORT = 6000
    IP_ADDRESS = '127.0.0.1'
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
    
    thread = Thread(target=receivedMsg)
    thread.start()
    
    
def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry
    
    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()
    
    SERVER.send(playerName.encode())
    
def recievedMsg():
    pass

def askPlayerName():
    global playerName 
    global nameEntry
    global nameWindow
    global canvas1
    
    nameWindow = Tk()
    nameWindow.title('Tambola Family Fun')
    nameWindow.geometry('800x688')
    
    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()
    
    bg = ImageTk.PhotoImage(file = 'C:/Users/MBajw/OneDrive/Documents/Coding.background_project.png')
    
    canvas1 = Canvas(nameWindow, widht = 500, height= 500)
    canvas1.pack(fill='both', expand= True)  
    
    canvas1.create_image(0,0, image= bg, anchor='nw')
    canvas1.create_text( screen_width/4.5, screen_height/8, text = 'Enter Name', font=('Chalkboard SE',60),fil='black')
    
    nameEntry = Entry(nameWindow, widht=15, justify='center', font= ('Chalkboard SE',30),bd=5, bg='white')  
    nameEntry.place(x= screen_width/7, y= screen_height/5.5)
    
    button = Button(nameWindow, text='Save', font= ('Chalkboard SE',30),width=11, command = saveName, height=2, bg= '#80deea',bd=3)
    button.place(x=screen_width/6, y = screen_height/4)
    
    nameWindow.resizable(True, True)
    nameWindow.mainloop()
