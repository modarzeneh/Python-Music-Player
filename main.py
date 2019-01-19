from tkinter import *
from pygame import mixer
from tkinter import messagebox
from tkinter import filedialog
import os
import pause

root = Tk()
root.geometry('300x350')


mixer.init()  ## initializing the mixer



### Functions ####
def play_music():
    if pause.paused == False:
        try:
            mixer.music.load(file_path)
            mixer.music.play()
            status_bar['text'] = "Playing..." + os.path.basename(file_path) ## show filename in the status_bar
        except:
            messagebox.showerror("Error","File Not Found, Please Open!")
    elif pause.paused == True:
        mixer.music.unpause()
        status_bar['text'] = "Playing..." + os.path.basename(file_path)
        
def pause_music():
    pause.paused = True
    mixer.music.pause()
    status_bar['text'] = "Paused..." + os.path.basename(file_path)
   
def stop_music():
    pause.paused = False
    mixer.music.stop()  ## Stop playing the file
    status_bar['text'] = os.path.basename(file_path)
        
def set_vol(val):
    volume = int(val) / 100 ## set_volume of mixer takes only values between 0 and 1
    mixer.music.set_volume(volume)
    

def open_file():
    global file_path
    file = filedialog.askopenfile(title="Open Song",filetypes=(("Mp3 Songs","*.mp3"),("All Files","*.*")))
    file_path = file.name
    
def about_cmd():
    messagebox.showinfo("About Us","Music Player Powered By Modar Zeneh")

######### Widggets ################### 

## Create an image Buttons ## 
img_play = PhotoImage(file="play.png")
img_stop = PhotoImage(file="stop.png")
img_pause = PhotoImage(file="pause.png")

## Create Buttons ##
btn_play = Button(root,image=img_play,command=play_music)
btn_play.pack(pady=5)
btn_stop = Button(root,image=img_stop,command=stop_music)
btn_stop.pack(pady=5)
btn_pause = Button(root,image=img_pause,command=pause_music)
btn_pause.pack(pady=5)

## Create Scale ##
scale = Scale(root,from_=0,to=100,orient=HORIZONTAL,width=20,command=set_vol)
scale.set(50) ## Set the default value of the scale to 50%
mixer.music.set_volume(0.5)
scale.pack(pady=5)

### Create the Menubar ###
menubar = Menu(root)
root.config(menu=menubar)
## Create the submenus ##
menu_file = Menu(menubar)
menu_help = Menu(menubar)
menu_file.add_command(label="Open File",command=open_file)
menu_file.add_command(label="Exit",command=root.destroy)
menu_help.add_command(label="About",command=about_cmd)

menubar.add_cascade(label="File",menu=menu_file)
menubar.add_cascade(label="Help",menu=menu_help)

## Create a Status Bar ###
status_bar =  Label(root,text="Welcome To Melody",relief='sunken')
status_bar.pack(side=BOTTOM,fill=X)





root.mainloop()

