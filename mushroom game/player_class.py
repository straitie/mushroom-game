from mushroom_class import Mushroom
from pathlib import Path

class PlayerData:
    def __init__(self):
        self.mushrooms = []
        self.progress = 0

    def save_data(self):
        path = Path(r'theomycology_save_data.txt')
        try:
            path.read_text()
        except FileNotFoundError:
            print("Error! Did you delete the save data file?")
        text = str(self.progress)+"\n"
        for item in self.mushrooms:
            text += str(item.aspect)+"\n"
        path.write_text(text)

    def load_data(self):
        path = Path(r'theomycology_save_data.txt')
        try:
            path.read_text()
        except FileNotFoundError:
            print("Error! Did you delete the save data file?")
        contents = path.read_text()
        lines = contents.splitlines()
        self.progress == int(lines[0])
        for i in range(1,len(lines)):
            self.mushrooms.append(Mushroom(lines[i]))

    def print_inv_mushrooms(self):
        print("Mushrooms")
        self.mushrooms.sort()
        for index, item in enumerate(self.mushrooms):
            print(f"{index+1}. {item}")

    def interact_mushrooms(self):
        self.print_inv_mushrooms()
        user_input_1 = int(input("Please type the numbers that you would like to breed, \nFirst: "))
        user_input_2 = int(input("Second: "))
        self.mushrooms.append(self.mushrooms[user_input_1-1].breed(self.mushrooms[user_input_2-1]))
