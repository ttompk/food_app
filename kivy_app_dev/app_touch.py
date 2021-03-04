import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty 
from kivy.graphics import Rectangle
from kivy.graphics import Color

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1,0,0,0.5)  # r,g,b,alpha
            self.rect = Rectangle(pos=(100,100), size=(50,50))

        self.btn  = Button()
    
    ## these work on any layout (grid, float, etc)
    # this overwrites the functionality
    def on_touch_down(self, touch):
        print("Mouse Down", touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        print("Mouse Up", touch)
        self.btn.opacity = 1

class Interact(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    Interact().run()
