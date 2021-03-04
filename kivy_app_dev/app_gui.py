import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# design
class Mygrid(GridLayout):
    def __init__(self, **kwargs):
        super(Mygrid, self).__init__(**kwargs)
        
        self.cols=1

        self.inside = GridLayout()
        self.inside.cols = 2
        
        self.inside.add_widget(Label(text="First:  "))
        self.fname = TextInput(multiline=False)
        self.inside.add_widget(self.fname)

        self.inside.add_widget(Label(text="Last:  "))
        self.lname = TextInput(multiline=False)
        self.inside.add_widget(self.lname)

        self.inside.add_widget(Label(text="Email:  "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        # add the inside grid to the overall grid
        self.add_widget(self.inside)

        self.submit = Button(text=" Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        first=self.fname.text
        last=self.lname.text
        email=self.email.text
        
        print("First: ", first, " Last: ", last, " Email", email)
        self.fname.text= ""
        self.lname.text= ""
        self.email.text= ""


# logic
class Myapp(App):
    ## init is inherited from App

    def build(self):
        return Mygrid()




if __name__ == "__main__":
    Myapp().run()
