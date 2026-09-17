
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label

class Pixel11ProCamera(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # Pixel 11 Pro 4K Camera
        self.cam = Camera(play=True, resolution=(1920, 1080))
        self.add_widget(self.cam)

        # Info Label
        self.info = Label(text="Pixel 11 Pro + S26 Ultra Style - 4K 60FPS", size
