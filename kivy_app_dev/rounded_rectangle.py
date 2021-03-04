from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.uix.floatlayout import FloatLayout

Config.set("graphics", "width", "320")
Config.set("graphics", "height", "480")

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1,0,0,0.5)  # r,g,b,alpha
            self.rect = Rectangle(pos=(100,100), size=(50,50))
    
    
        self.btn = Button()

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


class RoundedCornerLayout(FloatLayout):
    def __init__(self):
        super().__init__()
        
        # adjust button size here (for all buttons)
        self.x_size=100
        self.y_size=100
        self.size_hint = (None, None)
        self.size = (self.x_size, self.y_size)
        
        self.pos_hint = {"x": 0.1, "y": 0.75}
        #self.radius = [( self.x_size/2, self.y_size/0.5),
        #    ( self.x_size/0.5, self.y_size/2 ), 
        #    ( self.x_size/2, self.y_size/2 ),
        #    ( self.x_size/2, self.y_size/2 )]


class Round_rect(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    Round_rect().run()