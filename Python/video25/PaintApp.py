from tkinter import *
import tkinter.font


class PaintApp:

    drawing_tool = 'text'
    left_but = 'up'
    x_pos, y_pos = None, None
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

    def left_but_down(self, event=None):

        self.left_but = 'down'

        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    def left_but_up(self, event=None):

        left_but = 'up'

        self.x_pos = None
        self.y_pos = None

        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawing_tool == 'line':
            self.line_draw(event)
        elif self.drawing_tool == 'arc':
            self.arc_draw(event)
        elif self.drawing_tool == 'oval':
            self.oval_draw(event)
        elif self.drawing_tool == 'rectangle':
            self.rectangle_draw(event)
        elif self.drawing_tool == 'text':
            self.text_box(event)

    def motion(self, event=None):

        if self.drawing_tool == 'pencil':
            self.pencil_draw(event)

    def pencil_draw(self, event=None):

        if self.left_but == 'down':
            
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos,
                                         event.x, event.y, smooth=True)

            self.x_pos = event.x
            self.y_pos = event.y

    def line_draw(self, event = None):

        if None not in (self.x1_line_pt, self.x2_line_pt, 
                        self.y1_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt,
                                    self.x2_line_pt, self.y2_line_pt,
                                    smooth=True, fill='green')   
    def arc_draw(self, event=None):

        if None not in (self.x1_line_pt,self.x2_line_pt,
                            self.y1_line_pt,self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,self.y2_line_pt
            event.widget.create_arc(coords, start=0, extent=150, style=ARC)

    def oval_draw(self, event=None):

        if None not in (self.x1_line_pt,self.x2_line_pt,
                            self.y1_line_pt,self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,self.y2_line_pt
            event.widget.create_oval(coords, fill='midnight blue', outline='yellow', 
                                        width=2) 

    def rectangle_draw(self, event=None):

        if None not in (self.x1_line_pt,self.x2_line_pt,
                            self.y1_line_pt,self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,self.y2_line_pt
            event.widget.create_rectangle(coords, fill='yellow', outline='midnight blue', 
                                        width=2)         
        
    def text_box(self, event=None):

        if None not in (self.x1_line_pt,self.y1_line_pt):
            text_font = tkinter.font.Font(family='Helvetica', size=20,
                                          weight='bold', slant='italic')

            event.widget.create_text(self.x1_line_pt, self.y1_line_pt,
                                    fill='green', font=text_font, text='hail')

    def __init__(self, root):

        drawing_area = Canvas(root)
        drawing_area.pack()
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

root = Tk()
paint_app = PaintApp(root)
root.mainloop()
