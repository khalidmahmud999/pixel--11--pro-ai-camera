from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.clock import Clock
import cv2
import numpy as np
import time, os

class Pixel11ProCamera(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # S26 Ultra Style 4K Camera
        self.cam = Camera(play=True, resolution=(3840, 2160), index=0)
        self.zoom_level = 1.0
        self.ois_enabled = True
        self.ai_mode = "Pixel 11 Pro"
        self.is_dslr = False
        
        self.add_widget(self.cam)

        # Label for info
        self.info = Label(text="Pixel 11 Pro + S26 Ultra OIS | Zoom: 1.0X | AI ON | 4K", size_hint_y
