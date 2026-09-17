from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
import time

class Pixel11ProCamera(BoxLayout):
    def __init__(self, **kw):
        super().__init__()
        self.orientation='vertical'

        self.info=Label(
            text='Pixel 11 Pro | 4K',
            size_hint=(1,.1)
        )
        self.add_widget(self.info)

        self.cam=
           
