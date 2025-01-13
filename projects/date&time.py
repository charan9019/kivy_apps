from datetime import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.lang import Builder

kv_code = ("""
<TimeAndDateScreen>:
    Label:
        id: TimeScreen
        text: " "
        font_size: 40
        size_hint: None,None
        pos:200,400
        

    Label:
        id: DateScreen
        text: " "
        font_size: 40
        size_hint: None,None
        pos:600,400
""")
Builder.load_string(kv_code) 

class makeApp (App):
    def build(self):
        self.root = TimeAndDateScreen()
        self.LoadDT()
        return self.root

    def LoadDT (self):
        self.root.LiveTime()
    
class TimeAndDateScreen(FloatLayout):
    def LiveTime(self, *args):
        def LiveLoop(dt):
           current_time = datetime.now().strftime('%I:%M:%S %p')
           current_date = datetime.now().strftime('%d-%m-%y')
           self.ids.TimeScreen.text = f'Time = {current_time}'
           self.ids.DateScreen.text = f'Date = {current_date}'

        Clock.schedule_interval(LiveLoop, 1)


if __name__== '__main__':
    makeApp().run() 
