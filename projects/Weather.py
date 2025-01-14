from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
import requests

kv_code =("""
<Weather_Screen>:
    canvas.before:
        Color:
            rgba: 0.2, 0.2, 0.2, 1
        Rectangle:
            pos:self.pos
            size:self.size
          

    Label:
        
        text:"Enter Your City >>> "
        size_hint:None,None
        size:200,300
        pos:300,280
        color:0,1,0,1
        italic:True      
    
    TextInput:
        id:city_input
        size_hint:None,None
        size:200,50
        pos:500,400
        multiline:False
         
          
    Button:
        text:"Get Weather"
        size_hint:None,None
        size:200,80
        pos:500,300
        on_press:root.getting()
          
    Label:
        id:result_screen
        text:" "
        size_hint:None,None
        size:200,300
        pos:500,500
        color:1,1,1,1
        font_name:'DejaVuSans'
        

""")
Builder.load_string(kv_code) 

class weather_app(App):
    def build (self):
        return Weather_Screen()
    

class Weather_Screen(FloatLayout):
    def getting(self, *args):
        city = self.ids.city_input.text
        api_key = '5689eb83c536fa5ecc4c5785b0b84743'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            weather = data['weather'][0]['description']
            self.ids.result_screen.text = f"temprature is : {temp}C\n condition is : {weather}"

        else :
            self.ids.result_screen.text = "not found"


if __name__=='__main__':
    weather_app().run()
