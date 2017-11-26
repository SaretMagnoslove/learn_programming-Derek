from tkinter import *
from PIL import Image, ImageTk

class TkInterEx:
    
    @staticmethod
    def quit_app(event=None):
        root.quit()

    def on_fav_food_select(self, event=None):

        lb_widget = event.widget

        index = int(lb_widget.curselection()[0])

        lb_value = lb_widget.get(index)

        self.fav_food_label['text'] = "I'll get you " + lb_value

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

        lb_frame = LabelFrame(root, text="Food Options", padx=5, pady=5)

        self.fav_food_label = Label(lb_frame,
                                    text="What is your favorite food")

        self.fav_food_label.pack()

        list_box = Listbox(lb_frame)

        list_box.insert(1, "Bahgol")
        list_box.insert(2, "Jumbo mollusk")
        list_box.insert(3, "Osol twist")
        list_box.insert(4, "Eelwasser")
        list_box.insert(5, "Regova egg")

        list_box.bind('<<ListboxSelect>>', self.on_fav_food_select)
        list_box.pack()

        lb_frame.pack()

        sb_frame = Frame(root)

        quantity_label = Label(sb_frame,
                                text='How many shall I replicate')
        
        quantity_label.pack()

        spin_box = Spinbox(sb_frame,
                            from_=1, to=5)
        
        spin_box.pack()

        extra_label = Label(sb_frame,
                            text='Select style')
        
        extra_label.pack()

        extras_spin_box = Spinbox(sb_frame,
                            values=('Vulcan',
                                    'Romulan',
                                    'Klingon'))
        
        extras_spin_box.pack()

        sb_frame.pack()

root = Tk()
root.geometry('600x550')
app = TkInterEx(root)
root.mainloop()



