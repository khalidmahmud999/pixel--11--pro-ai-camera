
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
import time
import os

class Pixel11ProCamera(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # Top Bar - S26 Ultra Style
        self.info = Label(
            text="Pixel 11 Pro | 4K 60FPS | AI HDR+ ON | 200MP",
            size_hint=(1, 0.1),
            font_size='14sp'
        )
        self.add_widget(self.info)

        # Main 4K Camera
        self.cam = Camera(play=True, resolution=(1920, 1080), index=0)
       
