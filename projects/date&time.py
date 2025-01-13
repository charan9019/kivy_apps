from datetime import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.lang import Builder

kv_code = ("""
<TimeAndDateScreen>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos:self.pos
            size:self.size
    Label:
        id: TimeScreen
        text: " "
        font_size: 40
        size_hint: None,None
        pos:200,400
        color:0,0,0,1
        italic: True
          
    Label:
        id: DateScreen
        text: " "
        font_size: 40
        size_hint: None,None
        pos:600,400
        color:0,0,0,1
        italic: True
           
    Widget:
        canvas:
            Color:
                rgba: 0.5, 0.5, 0.5, 1
            Rectangle:
                pos:450,700
                size:300,100
            Color:
                rgba: 0, 0, 0, 0.5
            Line:
                width: 2
                rectangle: 450, 700, 300, 100
           
    Label:
        text: "Date and Time"
        font_size: 30
        size_hint: None, None
        pos: 450,700
        size: 300, 100
        italic: True
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
