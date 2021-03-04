import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

'''
# design
class RoundedCornerLayout(FloatLayout):
    def __init__(self):
        super().__init__()
        self.size_hint = (None, None)
        self.size = (400, 200)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
'''

# logic
class Floating(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    Floating().run()
