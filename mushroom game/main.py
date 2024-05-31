from player_class import *
from mushroom_class import *
from mushroom_test_class import *

def main():
    print("""Welcome to Theomycology!
Would you like to:
1. Play new game
2. Load save
3. Exit""")
    while True:
        player = PlayerData()
        user_input = int(input(">"))
        if user_input == 1:
            start_new_game(player)
            break
        elif user_input == 2:
            loaded_save(player)
            break
        elif user_input == 3:
            break

def fail(player):
    print(f"You failed! You made it to level {player.progress}")

def puzzle_1(player):
    player.progress = 1
    question = ""
    print(f"Puzzle one is: {question}")
    puzzle_one = MushroomTest(1,["Electric"])
    while True:
        print("""Enter number of option
1. Breed Mushrooms
2. Enter mushroom into slot
3. Submit answer
4. Reread question
5. Save data
6. exit game without saving""")
        user_input = ""
        try:
            user_input = int(input(">"))
        except ValueError:
            print("Invalid input")
        match user_input:
            case 1:
                player.interact_mushrooms()
            case 2:
                while True:
                    print("1. Slot\n2. Exit")
                    try:
                        user_input = int(input(">"))
                    except ValueError:
                        print("Invalid input")
                    if user_input == 2:
                        break
                    elif user_input == 1:
                        while True:
                            print("Which mushroom?")
                            player.print_inv_mushrooms()
                            try:
                                user_input = int(input(">"))
                            except ValueError:
                                print("Invalid input")
                            if user_input < len(player.mushrooms) and user_input > 0:
                                mushroom = str(player.mushrooms[user_input-1])
                                puzzle_one.enter_slot(mushroom,1)
                                break
                            else:
                                print("Not in list.")
                        break
            case 3:
                puzzle_one.make_attempt()
                if puzzle_one.attempts_left <= 0:
                    fail()
                    

def start_new_game(player):
    print("Welcome Message, fire, earth mushrooms added")
    player.mushrooms.append(Mushroom("Fire"))
    player.mushrooms.append(Mushroom("Earth"))
    puzzle_1(player)

def loaded_save(player):
    player.load_save()
    match player.progress:
        case 0:
            print("No saved data, starting new game")
        case 1:
            puzzle_1(player)

if __name__ == "__main__":
    main()
