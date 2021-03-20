#####
# Food Expiration APP
# GUI
#####

# set the window backend - by default it's egl_rpi
# it's 'already in use' by the machine.
# Settings that likly will work with a screen: window="egl_rpi", backend="gl"
import os
os.environ['KIVY_WINDOW']="egl_rpi" #egl_rpi #sdl2 #pygame #x11
os.environ['KIVY_GL_BACKEND']="gl" #gl  #glew #sdl2 #angle_sdl2 #mock
#os.environ['KIVY_BCM_DISPMANX_ID']="0"
os.environ['KIVY_GL_DEBUG']="0"

# the environment variables need to be set before importing kivy
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.clock import Clock

# database 
import sqlite3
import datetime as dt

# global database dictionary
DB_DICT = {} 


def sql_connect(sqlite_filename='foodDB.db'):
    ''' conncect to sqlite database '''
    # add auth as needed in future
    try:
        con = sqlite3.connect(sqlite_filename)
        print("connected to db")
        return con
    except:
        print("failed db connection.")


def sql_insert():
    ''' insert row into sqlite database '''
    # labels table columns: id, entry_time, entry_method, food_type, expire_date, pic, pred_food, prob_food
    # NOTE: id should be autoincrementing
    try:
        con = sql_connect()
        cur = con.cursor()
        print("Inserting into sql db.")  # for dev only
        insert_string = ""               # clear out value

        # add timestamp
        DB_DICT['entry_time'] = str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # sqlite command string
        insert_string = f"INSERT INTO labels ({','.join(DB_DICT.keys())}) VALUES ({','.join(DB_DICT.values())})"
        print(insert_string)  # dev only
        #cur.execute(insert_string)
        #con.commit()
        con.close()
        print("Connection closed.")  # for dev only
    except:
        print("db entry failed.")
    finally:
        DB_DICT.clear()  # set variables from the dict to none

class MainWindow(Screen):
    # First screen on launch

    '''
    # The following functions replaced with user_input
    def expire_btn(self):
        print(self.var_btn_expires.text)

    def open_btn(self):
        self.user_input(self.var_btn_opened)

    def today_btn(self):
        self.user_input(self.var_btn_close.text)
    '''

    def show_popup(self):
        x=ShowPopup()

    def user_input(self, main_val):
        # button pushed
        self.main_val = main_val.text
        print(self.main_val)  # for dev only
        DB_DICT['label_type'] = self.main_val

        # add entry method: gui vs vocal
        DB_DICT['entry_method'] = 'gui'

        # today's date label goes straight to database
        if self.main_val in ["Print Today's Date", "Opened"]:
            sql_insert()

        App.get_running_app().user_select.append(self.main_val)


class DaysWindow(Screen):
    # Number of days when the product expires
    def __init__(self, **kwargs):
        super(DaysWindow, self).__init__(**kwargs)
        self.var_days=None

    def btn_days(self, var_days):
        self.var_days = var_days
        print(self.var_days)  # for dev only
        expire_date_val = ( dt.datetime.now() + dt.timedelta(days=int(self.var_days))).strftime("%Y-%m-%d %H:%M:%S")
        DB_DICT['expire_date'] = str(expire_date_val)

    def main_go_back(self):
        App.get_running_app().user_select[0]=""
        DB_DICT['label_type'] = None
        #self.var_days = ""


class FoodWindow(Screen):
    # Select food type
    def food_val_func(self, food_val):
        self.food_val = food_val.text
        print(self.food_val)  # for dev only
        DB_DICT['food_type'] = self.food_val

    def days_go_back(self):
        App.get_running_app().user_select[1]=""
        self.var_food = ""
        DB_DICT['expire_date'] = None

    def show_popup(self):
        x=ShowPopup()


class SettingsWindow(Screen):
    # display settings options
    def wifi_val_func(self, wifi_val):
        self.wifi_val = wifi_val.text
        print(self.wifi_val)

    def sleep_val_func(self, sleep_val):
        self.sleep_val = sleep_val.text
        print(self.sleep_val)

    def volume_val_func(self, volume_val):
        self.volume_val = volume_val.text
        print(self.volume_val)

    def main_go_back(self):
        App.get_running_app().user_select[0]=""

    def show_popup_wifi(self):
        x=ShowPopupWifi()


class ShowPopup():

    def __init__(self):
        show = P()
        self.popupWindow = Popup(
            title="Printing Label",
            title_size=24,
            content=show,
            size_hint=(None,None),
            size=(200,200))
        self.popupWindow.open()
        Clock.schedule_once(lambda dt: self.dismiss_popup(), 3)

    def dismiss_popup(self):
        self.popupWindow.dismiss()

class ShowPopupWifi():
     def __init__(self):
        show = PopupWifi()
        self.popupWindow = Popup(
            title="Wifi Details",
            title_size=24,
            content=show,
            size_hint=(None,None),
            size=(200,200))
        self.popupWindow.open()
        Clock.schedule_once(lambda dt: self.dismiss_popup(), 3)

     def dismiss_popup(self):
        self.popupWindow.dismiss()

class WindowManager(ScreenManager):
    pass


# layout design
class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)
        ### main screen
        var_btn_expires = ObjectProperty(None)
        var_btn_opened = ObjectProperty(None)
        var_btn_today = ObjectProperty(None)
        var_btn_settings = ObjectProperty(None)

        ### days screen
        # none defined

        ### food screen
        var_btn_meat = ObjectProperty(None)
        var_btn_vegie = ObjectProperty(None)
        var_btn_dairy = ObjectProperty(None)

        ### settings screen
        var_btn_wifi = ObjectProperty(None)
        var_btn_wifi_info = ObjectProperty(None)
        var_btn_sleep = ObjectProperty(None)
        var_btn_volume = ObjectProperty(None)

        ### to print a square to the screen - puts it over whats in .kv file
        #with self.canvas:
        #    Color(1,0,0,0.5)  # r,g,b,alpha
        #    self.rect = Rectangle(pos=(100,100), size=(50,50))

class P(FloatLayout):
    pass

class PopupWifi(FloatLayout):
    pass

# associated kivy file
# this file contains the layout information - critical.
kv = Builder.load_file("my.kv")

# logic
class ExpireApp(App):
    ## init is inherited from App
    user_select=[]

    def build(self):
        #Window.size = (240, 240)
        Window.clearcolor = (1,1,1,1)
        return kv

    def on_stop(self):
        #print(f"\GraphInputKivyApp.non_stop: self.graphListOfXY")
        print(self.user_select)

if __name__ == "__main__":
    ExpireApp().run()
    #print(ExpireApp.user_select)
