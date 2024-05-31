class Mushroom:
    mushroom_breed_dict = {
        "Fire": {"Water": "Air", "Earth": "Metal", "Electric": "Light"},
        "Water": {"Fire": "Air", "Life": "Animal", "Metal": "Ice"},
        "Earth": {"Fire": "Metal", "Metal": "Electric"},
        "Metal": {
            "Electric": "Magnetic",
            "Water": "Ice",
            "Ice": "Crystal",
            "Poisonous": "Corrosive",
        },
        "Electric": {"Metal": "Magnetic", "Fire": "Light"},
        "Life": {"Water": "Animal", "Light": "Healing"},
        "Poisonous": {"Metal": "Corrosive", "Light": "Dark"},
        "Ice": {"Metal": "Crystal"},
        "Light": {"Poisonous": "Dark"},
        "Corrosive": {"Dark": "Entropic"},
        "Dark": {"Corrosive": "Entropic"},
    }

    def __init__(self, aspect: str):
        self.aspect = aspect
    
    def __str__(self):
        return self.aspect + " Mushroom"
    
    def __lt__(self, mushroom_two):
        if str(self) < str(mushroom_two):
            return True
        else:
            return False

    def breed(self, mushroom_two):
        if (
            self.aspect in Mushroom.mushroom_breed_dict
            and mushroom_two.aspect in Mushroom.mushroom_breed_dict[self.aspect]
        ):
            mushroom_bred = Mushroom(
                Mushroom.mushroom_breed_dict[self.aspect][mushroom_two.aspect]
            )
            print(f"Successfully bred a {mushroom_bred}!")
            return mushroom_bred
        else:
            print("Nothing happens")