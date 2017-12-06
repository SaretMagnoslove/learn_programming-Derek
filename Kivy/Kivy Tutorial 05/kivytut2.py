import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string(''' 
<ScreenOne>:
    BoxLayout:
        Button:
            text: "Go to screen Two"
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 1
                root.manager.current = "screen_two"
<ScreenTwo>:
    BoxLayout:
        Button:
            text: "Go to screen one"
            on_press:
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 1
                root.manager.current = "screen_one"
 ''')

class ScreenOne(Screen):
     pass
class ScreenTwo(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))

class KivyTut2App(App):

    def build(self):
        return screen_manager

sampleApp = KivyTut2App()
sampleApp.run()