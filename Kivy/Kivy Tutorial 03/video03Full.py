# ---------- main.py  ---------- 

import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout):

    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()

# ---------- calculator.kv  ----------

# Custom button
<CustButton@Button>:
    font_size: 32

# Define id so I can refer to the CalcGridLayout
# class functions
# Display points to the entry widget
<CalcGridLayout>:
    id: calculator
    display: entry
    rows: 5
    padding: 10
    spacing: 10

    # Where input is displayed
    BoxLayout:
        TextInput:
            id: entry
            font_size: 32
            multiline: False

    # When buttons are pressed update the entry
    BoxLayout:
        spacing: 10
        CustButton:
            text: "7"
            on_press: entry.text += self.text
        CustButton:
            text: "8"
            on_press: entry.text += self.text
        CustButton:
            text: "9"
            on_press: entry.text += self.text
        CustButton:
            text: "+"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "4"
            on_press: entry.text += self.text
        CustButton:
            text: "5"
            on_press: entry.text += self.text
        CustButton:
            text: "6"
            on_press: entry.text += self.text
        CustButton:
            text: "-"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "1"
            on_press: entry.text += self.text
        CustButton:
            text: "2"
            on_press: entry.text += self.text
        CustButton:
            text: "3"
            on_press: entry.text += self.text
        CustButton:
            text: "*"
            on_press: entry.text += self.text

    # When equals is pressed pass text in the entry
    # to the calculate function
    BoxLayout:
        spacing: 10
        CustButton:
            text: "AC"
            on_press: entry.text = ""
        CustButton:
            text: "0"
            on_press: entry.text += self.text
        CustButton:
            text: "="
            on_press: calculator.calculate(entry.text)
        CustButton:
            text: "/"
            on_press: entry.text += self.text