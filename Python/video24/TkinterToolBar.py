from tkinter import *
from PIL import Image, ImageTk

class TkInterEx:
    @staticmethod
    def quit_app(event=None):
        root.quit()

    def __init__(self, root):

        root.title("Python based ToolBar example")

        menubar = Menu(root)

        file_menu = Menu(root, tearoff=0)
        file_menu.add_command(label='Open')
        file_menu.add_command(label='Save')
        file_menu.add_command(label='Exit', command=self.quit_app)

        menubar.add_cascade(label='File', menu='file_menu')

        toolbar = Frame(root, bd=1, relief=RAISED)

        open_img = Image.open("open.png")
        save_img = Image.open("disk.png")
        exit_img = Image.open("exit.png")

        open_icon = ImageTk.PhotoImage(open_img)
        save_icon = ImageTk.PhotoImage(save_img)
        exit_icon = ImageTk.PhotoImage(exit_img)

        open_button = Button(toolbar, image=open_icon)
        save_button = Button(toolbar, image=save_icon)
        exit_button = Button(toolbar, image=exit_icon,
                            command=self.quit_app)

        open_button.image = open_icon
        save_button.image = save_icon
        exit_button.image = exit_icon

        open_button.pack(side=LEFT, padx=2, pady=2)
        save_button.pack(side=LEFT, padx=2, pady=2)
        exit_button.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        root.config(menu=menubar)

root = Tk()
root.geometry('600x550')
app = TkInterEx(root)
root.mainloop()



