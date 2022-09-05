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



class MyGridLayout(Widget):
    # initialize infinite keywords

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # Print to Screen
        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite pizza is {color}!'))

        # Print to cmd
        print(f'Hello {name}, you like {pizza} pizza, and your favorite pizza is {color}!')

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class AwesomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__' :
    AwesomeApp().run()