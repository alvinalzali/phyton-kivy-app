# boxes and inputs
import kivy 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.label import Label

# Designate Our .kv design file (compatible with dir path)
#method 1 with diff file
Builder.load_file('color.kv') 

# method 2 with string 
# Builder.load_string('''  use design here ''') 



class Mylayout(Widget):
    # initialize infinite keywords
    pass

class AwesomeApp(App):
    def build(self):
        return Mylayout()

if __name__ == '__main__' :
    AwesomeApp().run()