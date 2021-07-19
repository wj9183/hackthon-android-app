import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import mysql.connector
from mysql.connector import Error
from hackathon_app import set_destination



class hackathonapp(toga.App):
    def startup(self):
        

        # name_label = toga.Label(
        #     'Your name: ',
        #     style=Pack(padding=(0, 5))
        # )
        # self.name_input = toga.TextInput(style=Pack(flex=1))

        # name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        # name_box.add(name_label)
        # name_box.add(self.name_input)
        
        button = toga.Button(
            '오래(orae)란',
            on_press=self.say_hello,
            
        )

        image_1_temp = toga.images.Image("C:\\Users\\5-4\\hackathon-app\\src\\hackathon_app\\images\\오래-001.png")
        image_1 = toga.ImageView(id='view_1',image=image_1_temp)

        main_box = toga.Box(style=Pack(direction=COLUMN))
        # main_box.add(button)
        # main_box.add(name_box)
        main_box.add(image_1)
        main_box.add(button)

        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def say_hello(self, widget):
        hi = set_destination.set_destination()
        print(hi)
        

def main():
    return hackathonapp()