import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutApp(App):
    
    def build(self):
        return BoxLayout()

blApp = BoxLayoutApp()
blApp.run()

