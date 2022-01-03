from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy_garden.graph import Graph, MeshLinePlot
from datetime import datetime
from math import exp


class MyApp(App):

    def build(self):
        root_widget = BoxLayout(orientation='vertical')

        pressure_graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                               x_ticks_major=25, y_ticks_minor=1,
                               y_grid_label=True, x_grid_label=True, padding=5,
                               x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)

        simple_grid = GridLayout(cols=1, size_hint_y=2)
        table_grid = GridLayout(cols=2, size_hint_y=1)
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

        l_button_1 = Button(text='Left Foot Reading ')
        
        left_grid.add_widget(l_button_1)
        

        # right row buttons
        r_button_1 = Button(text='Right Foot Reading ')
        
        right_grid.add_widget(r_button_1)
       

        def btn_press(instance):
            try:
                multiplier = 0.5
                side = instance.text.split("_")[0]
                if side == 'r':

                    multiplier = 1
                    data_length = 150
                    right_plot = MeshLinePlot(color=[1, side, 0, 1])
                    pressure_graph.remove_plot(right_plot)
                    pressure_graph.clear_buffer()
                    custom_string = instance.text.split(" ")[2]
                    custom_value = multiplier * int(custom_string)
                    right_plot.points = [(x, exp(x/custom_value))
                                         for x in range(0, data_length)]
                    pressure_graph.add_plot(right_plot)
                else:
                    data_length = 150
                    left_plot = MeshLinePlot(color=[1, side, 0, 1])
                    pressure_graph.remove_plot(left_plot)
                    pressure_graph.clear_buffer()
                    custom_string = instance.text.split(" ")[2]
                    custom_value = multiplier * int(custom_string)
                    left_plot.points = [(x, exp(x/custom_value))
                                        for x in range(0, data_length)]
                    pressure_graph.add_plot(left_plot)
                print(custom_string + str(multiplier))
            except SyntaxError:
                print('Python syntax error!')
        root_widget.add_widget(simple_grid)

        l_button_1.bind(on_press=btn_press)
        

        r_button_1.bind(on_press=btn_press)
       

        return root_widget