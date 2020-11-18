from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('SUBTITRON')
root.geometry("500x300")


def open_file():
    subtitle_file = filedialog.askopenfilename(initialdir = "C:/Users",title="Open File", filetypes=(("Subtitle Files","*.srt"),))
    subtitle_file = open(subtitle_file,'r+')
    my_list = subtitle_file.readlines()
    print(my_list)

    count = 0
    for i in my_list:
        if "ã" in i:
            count+=1
            my_list = subtitle_file.replace('ã','ă')

    print("apare de : ")
    print(count)
    print(my_list)





open_btn = Button(root, text="Open File", command = open_file)
open_btn.pack(pady=20)


root.mainloop()