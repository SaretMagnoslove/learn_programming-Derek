from tkinter import *
from tkinter import ttk
import sqlite3


class studentDB:

    db_conn = 0
    theCurser = 0
    curr_student = 0

    def setup_db(self):

        self.db_conn = sqlite3.connect('student.db')
        self.theCurser = self.db_conn.cursor()
        try:
            self.db_conn.execute('CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY\
        AUTOINCREMENT NOT NULL, Fname TEXT NOT NULL, Lname TEXT NOT NULL);')
            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("ERROR : Table Not Created")

    def stud_submit(self):

        self.db_conn.execute("INSERT INTO Students(Fname, Lname) " +
                             "VALUES ('" +
                             self.fn_entry_value.get() + "', '" +
                             self.ln_entry_value.get() + "')")
        self.fn_entry.delete(0, 'end')
        self.ln_entry.delete(0, 'end')
        self.update_listbox()

    def update_listbox(self):

        self.list_box.delete(0, 'end')
        try:
            result = self.theCurser.execute(
                "SELECT ID, Fname, Lname FROM Students")
            for row in result:
                student_id = row[0]
                student_fname = row[1]
                student_lname = row[2]
                self.list_box.insert(student_id,
                                 student_fname + " " +
                                 student_lname)
        except sqlite3.OperationalError:
            print('Seems the table does not exist')
        except:
            print("1: couldn't retrieve Data")

    def load_student(self, event=None):

        lb_widget = event.widget
        index = str(lb_widget.curselection()[0] + 1)
        self.curr_student = index

        try:
            result = self.theCurser.execute("SELECT ID, Fname, Lname FROM Students\
        WHERE ID=" + index)

            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]

                self.fn_entry_value.set(stud_fname)
                self.ln_entry_value.set(stud_lname)

        except sqlite3.OperationalError:
            print('Seems the table does not exist')
        except:
            print("2: couldn't retrieve Data")

    def update_student(self, event=None):

        try:
            self.db_conn.execute("UPDATE Students SET Fname='" +
                                 self.fn_entry_value.get() +
                                 "', Lname='" +
                                 self.ln_entry_value.get() +
                                 "' WHERE ID=" + 
                                 self.curr_student)
            self.db_conn.commit()
        except sqlite3.OperationalError:
            print('Seems the table could not been updated')
        except:
            print("3: couldn't Update Data")
        
        self.fn_entry.delete(0, 'end')
        self.ln_entry.delete(0, 'end')

        self.update_listbox()
        
    def __init__(self, root):

        root.title("Python Based Student DB")
        root.geometry("300x350")

        #  1st Row

        fn_label = Label(root, text="First Name")
        fn_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.fn_entry_value = StringVar(root, value="")
        self.fn_entry = ttk.Entry(root,
                                  textvariable=self.fn_entry_value)
        self.fn_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        #  2ed Row

        ln_label = Label(root, text="Last Name")
        ln_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.ln_entry_value = StringVar(root, value="")
        self.ln_entry = ttk.Entry(root,
                                  textvariable=self.ln_entry_value)
        self.ln_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        #  3ed Row

        self.submit_button = ttk.Button(root,
                                        text="submit",
                                        command=lambda: self.stud_submit())
        self.submit_button.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.update_button = ttk.Button(root,
                                        text="update",
                                        command=lambda: self.update_student())
        self.update_button.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        #  4th Row

        scrollbar = Scrollbar(root)
        self.list_box = Listbox(root)
        self.list_box.bind('<<ListboxSelect>>', self.load_student)
        self.list_box.insert(1, 'Students Here')
        self.list_box.grid(row=3, column=0, columnspan=4,
                           padx=10, pady=10, sticky=W + E)

        self.setup_db()
        self.update_listbox()


root = Tk()
studDB = studentDB(root)
root.mainloop()
