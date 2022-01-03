from kivy.app import App  
       


from kivy.uix.tabbedpanel import TabbedPanel
  

from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('overview.kv')
# Create Tabbed class 
class Tab(TabbedPanel):
    pass
   
# create App class
class TabbedPanelApp(App):
    def build(self):
        return Tab()
  
# run the App
if __name__ == '__main__':
    TabbedPanelApp().run()
