from kivy.app import App  

from kivy.uix.widget import Widget 

from kivy.lang import Builder



Builder.load_file('switch.kv.yml')
# Create Tabbed class 
class MyLayout(Widget):
    pass
   
# create App class
class SwitchApplication(App):
    def build(self):
        return MyLayout()
  
# run the App
if __name__ == '__main__':
    MyLayout().run()
