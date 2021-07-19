import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import mysql.connector
from mysql.connector import Error
from hackathon_app import set_destination


class hackathonapp(toga.App):
    def startup(self):
        
        main_box = toga.Box(style=Pack(direction=COLUMN))
        

        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        image_1 = toga.ImageView(id='view_1',image='images\오래-001.png')
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            '경로',
            on_press=self.destination,
            style=Pack(padding=5)
        )

        main_box.add(image_1, button)
        main_box.add(name_box)
        # main_box.add(button)
        print('hi')

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def destination(self, widget):
        hi = set_destination.set_destination()
        print(hi)

def main():
    return hackathonapp()    