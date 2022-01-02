from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy_garden.graph import Graph, MeshLinePlot
from datetime import datetime
from pymongo import MongoClient
from math import sin


class MyApp(App):

    def build(self):
        root_widget = BoxLayout(orientation='vertical')

        pressure_graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                               x_ticks_major=25, y_ticks_major=1,
                               y_grid_label=True, x_grid_label=True, padding=5,
                               x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)

        simple_grid = GridLayout(cols=1, size_hint_y=2)
        table_grid = GridLayout(cols=2, size_hint_y=2)
        left_grid = GridLayout(cols=1, size_hint_y=1)
        right_grid = GridLayout(cols=1, size_hint_y=1)
        left_row = TextInput(text='Left', readonly=True)
        right_row = TextInput(text='Right', readonly=True)

        simple_grid.add_widget(pressure_graph)
        simple_grid.add_widget(table_grid)
        table_grid.add_widget(left_grid)
        table_grid.add_widget(right_grid)
        left_grid.add_widget(left_row)
        right_grid.add_widget(right_row)

        # Left row buttons
        for i in range(1, 4):
            left_grid.add_widget(Button(text='Reading ' + str(i)))
        # right row buttons
        for i in range(1, 4):
            right_grid.add_widget(Button(text='Reading ' + str(i)))

        def button_press(instance):
            try:

                data_length = 150
                plot = MeshLinePlot(color=[1, 0, 0, 1])
                custom_string = instance.text.split(" ")[1]
                if isinstance(instance, left_grid):
                    multiplier = 2
                custom_value = multiplier * int(custom_string)
                plot.points = [(x, sin(x, custom_value))
                               for x in range(0, data_length)]
                pressure_graph.add_plot(plot)
            except SyntaxError:
                print('Python syntax error!')
        root_widget.add_widget(simple_grid)

        return root_widget


MyApp().run()
