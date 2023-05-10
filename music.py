import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer


root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background='#0f1a2b')
root.resizable(False, False)

mixer.init()




def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()



image_icon = PhotoImage(
    file="icons8-audio-wave-48.png")
root.iconphoto(False, image_icon)

Top =PhotoImage(
    file="sound-wave.png")
Label(root, image=Top, bg="#0f1a2b").pack()


logo = PhotoImage(
    file="listen.png")
Label(root, image=logo, bg="#0f1a2b", bd=0).place(x=40, y=30)


ButtonPlay = PhotoImage(
    file="play.png")
Button(root, image=ButtonPlay, bg="#0f1a2b", bd=0,
       command=PlayMusic).place(x=115, y=300)

ButtonStop = PhotoImage(
    file="stop.png")
Button(root, image=ButtonStop, bg="#0f1a2b", bd=0,
       command=mixer.music.stop).place(x=30, y=400)

ButtonResume = PhotoImage(
    file="end.png")
Button(root, image=ButtonResume, bg="#0f1a2b", bd=0,
       command=mixer.music.unpause).place(x=115, y=400)

ButtonPause = PhotoImage(
    file="pause.png")
Button(root, image=ButtonPause, bg="#0f1a2b", bd=0,
       command=mixer.music.pause).place(x=200, y=400)


Menu = PhotoImage(file="menu.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=328, y=250, width=570, height=300)

Button(root, text="Open Folder", width=15, height=2, font=("times new roman",
       10, "bold"), fg="White", bg="#FFE000", command=AddMusic).place(x=329, y=189)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=500, font=("Times new roman", 10), bg="#ebb8dd", fg="white", selectbackground="lightblue", cursor="hand2", bd=4, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)



root.mainloop()