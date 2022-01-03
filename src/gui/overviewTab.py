from kivy.app import App  
from kivy.uix.tabbedpanel import TabbedPanel 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label


Builder.load_file('overview.kv.yml')
# Create Tabbed class 
class Tab(TabbedPanel):
    pass
   
# create App class
class MonitoringApplication(App):
    def build(self):
        lbl = Label(text ="Label is Added on screen !!:):)")
        return Tab()
  
# run the App
if __name__ == '__main__':
    MonitoringApplication().run()
