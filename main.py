
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
   text='Pixel 11 Pro',
   size_hint=(1,.1)
  )
  self.add_widget
