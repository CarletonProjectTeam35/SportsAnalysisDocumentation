from kivy.app import App  
from kivy.uix.widget import Widget 
from kivy.lang import Builder



Builder.load_file('switch.kv.yml')
# Create Tabbed class 
class MyLayout(Widget):
    def switch_click(self, switchObject, SwitchValue):
        if(SwitchValue):
            self.ids.my_label.text = "You are now in Skater mode"
        else:
            self.ids.my_label.text = "You are in Shooter mode"
            ##self.ids.myswitch.something = place holder value to switch between data
# create App class
class SwitchApplication(App):
    def build(self):
        return MyLayout()
  
# run the App
if __name__ == '__main__':
    SwitchApplication().run()
