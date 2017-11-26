from tkinter import *
from PIL import Image, ImageTk

class TkInterEx:
    @staticmethod
    def quit_app(event=None):
        root.quit()

    # Handles events on list box
    def on_fav_food_select(self, event=None):

        lb_widget = event.widget

        # Get index selected
        index = int(lb_widget.curselection()[0])

        # Get value selected in list box
        lb_value = lb_widget.get(index)

        self.fav_food_label['text'] = "I'll get you " + lb_value

    def __init__(self, root):

        root.title("Toolbar Example")

        # ---------- Create Menu Bar ----------

        # Create menu object
        menubar = Menu(root)

        # Create drop down menu
        file_menu = Menu(root, tearoff=0)

        # Add menu drop down options
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Exit", command=self.quit_app)

        # Add drop down options to File
        menubar.add_cascade(label="File", menu=file_menu)

        # ---------- Create Toolbar ----------

        # RAISED draws a line under the tool bar and bd defines the border width
        toolbar = Frame(root, bd=1, relief=RAISED)

        # Get images for toolbar
        open_img = Image.open("open.png")
        save_img = Image.open("disk.png")
        exit_img = Image.open("exit.png")

        # Create a TkInter image to be used in the button
        open_icon = ImageTk.PhotoImage(open_img)
        save_icon = ImageTk.PhotoImage(save_img)
        exit_icon = ImageTk.PhotoImage(exit_img)

        # Create buttons for the toolbar
        open_button = Button(toolbar, image=open_icon)
        save_button = Button(toolbar, image=save_icon)
        exit_button = Button(toolbar, image=exit_icon, command=self.quit_app)

        open_button.image = open_icon
        save_button.image = save_icon
        exit_button.image = exit_icon

        # Place buttons in the interface
        open_button.pack(side=LEFT, padx=2, pady=2)
        save_button.pack(side=LEFT, padx=2, pady=2)
        exit_button.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)

        root.config(menu=menubar)

        # ---------- Create a List Box ----------
        # A listbox displays a list of items to select

        # A label frame is a frame with a label
        lb_frame = LabelFrame(root, text="Food Options", padx=5, pady=5)

        # This label changes based on list box selections
        self.fav_food_label = Label(lb_frame,
                               text="What is your favorite food")

        self.fav_food_label.pack()

        list_box = Listbox(lb_frame)

        # Create list box options
        list_box.insert(1, "Spaghetti")
        list_box.insert(2, "Pizza")
        list_box.insert(3, "Burgers")
        list_box.insert(4, "Hot Dogs")

        # When a list box option is clicked execute the function
        list_box.bind('<<ListboxSelect>>', self.on_fav_food_select)

        list_box.pack()

        lb_frame.pack()

        # ---------- Create a Spin Box ----------
        # Provides a fixed number of values as an option

        sb_frame = Frame(root)

        quantity_label = Label(sb_frame,
                               text="How many do you want")

        quantity_label.pack()

        # Allow for the values 1 through 5
        spin_box = Spinbox(sb_frame,
                           from_=1, to=5)
        spin_box.pack()

        extras_label = Label(sb_frame,
                             text="Add on Item")

        extras_label.pack()

        # Add a list of custom items
        extras_spin_box = Spinbox(sb_frame,
                                  values=('French Fries',
                                          'Onion Rings',
                                          'Tater Tots'))

        extras_spin_box.pack()


        sb_frame.pack()

root = Tk()
root.geometry("600x550")
app = TkInterEx(root)
root.mainloop()