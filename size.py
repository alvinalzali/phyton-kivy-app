# boxes and inputs
import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # initialize infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 120
        self.colu_force_default = True
        self.colu_default_width = 120

        # Create second layout
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=200
        )
        self.top_grid.cols = 2


        # Add Widgets

        self.top_grid.add_widget(Label(text="Name: ",
            size_hint_y=None,
            height=50,
            size_hint_x=None,
            width=200)
        )
        # Add Input Box
        self.name = TextInput(multiline=True,
                              size_hint_y=None,
                              height=50,
                              size_hint_x=None,
                              width=200)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        # Add Input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favorite Color: "))
        # Add Input Box
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # Add new top_grid to app
        self.add_widget(self.top_grid)



        # Create Submit Button
        self.submit = Button(text="Submit", 
            font_size=29,
            size_hint_y=None,
            height=50,
            size_hint_x=None,
            width=200)

        # Bind Button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
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

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__' :
    MyApp().run()