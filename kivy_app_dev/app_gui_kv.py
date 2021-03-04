import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# design
class Mygrid(Widget):
    var_name = ObjectProperty(None)
    var_email = ObjectProperty(None)
    
    def btn(self):
        print("Name: ", self.var_name.text, "Email: " , self.var_email.text)
        self.var_name.text = ""
        self.var_email.text = ""

# logic
class Myapp(App):
    ## init is inherited from App

    def build(self):
        return Mygrid()


if __name__ == "__main__":
    Myapp().run()
