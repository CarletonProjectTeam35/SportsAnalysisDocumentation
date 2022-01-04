from kivy.app import App
  
# The GridLayout arranges children in a matrix.
# It takes the available space and divides
# it into columns and rows, then adds
# widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout
  
# Builder is a global Kivy instance used
# in widgets that you can use to load other
# kv files in addition to the default ones.
from kivy.lang import Builder
  
  
# Loading Multiple .kv files 
Builder.load_file('box1.kv.yml')
Builder.load_file('box2.kv.yml')
Builder.load_file('box3.kv.yml')

  
  
# Creating main kv file class
class main_kv(GridLayout):
    pass
  
# Create App class
class MainApp(App):
    def build(self):
        self.x = 150
        self.y = 400
        return main_kv()
  
# run the App
if __name__=='__main__':
    MainApp().run()