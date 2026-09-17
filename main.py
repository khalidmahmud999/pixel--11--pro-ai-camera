from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
import time

class Cam(BoxLayout):
 def __init__(self,**k):
  super().__init__(**k)
  self.orientation='vertical'
  self.t=Label(
   text='Pixel
