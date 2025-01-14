from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.lang import Builder


class MakeApp(App):
    def build(self):
        layout = GridLayout(cols=1)
        view = MapView(zoom=10, lat=13.3134, lon=76.2566)
        view.add_widget(MapMarkerPopup(lat=13.3134,lon=76.2566))
        return view

if __name__=='__main__':
    MakeApp().run()
