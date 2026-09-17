  from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
import time
import os

class Pixel11ProCamera(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.orientation = 'vertical'
        
        self.info = Label(
            text='Pixel 11 Pro | 4K 60FPS | AI',
