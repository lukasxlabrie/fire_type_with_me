import os

# keeps terminal clean for mac or pc
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# greets the player and explains the game
def introduction():
    print("Welcome to Twin Peaks: Fire Type With Me!")
    name = input("Enter your last name:")
    print(f"Welcome, Special Agent {name}. Your mission is to find Special Agent Dale Cooper and escort him out of Twin Peaks.")
    print("Explore the following locations to locate crucial items he may have left behind:")
    print("The Great Northern Hotel, The Double R Diner, The Roadhouse, One-Eyed Jacks, The Sheriff's Station, The Owl Cave, and The Black Lodge.")
    input("Press Enter to view controls...")

# shows the player the control scheme
def display_controls():
    print("Controls:")
    print("ENTER 'N', 'S', 'E', or 'W' to move between rooms.")
    print("ENTER 'Get [Item Name]' to pick up items.")
    print("ENTER 'Quit' to end the game.")
    print("*** Be sure to pay attention to lower/upper case letters when entering commands ***")
    input("Press Enter to start your investigation...")

# allows player to see which rooms they can travel to
def display_adjacent_rooms(current_room, rooms):
    adjacent_rooms = {k: v for k, v in rooms[current_room].items() if k in
    ['N','S','E','W']}
    print(f"Welcome to {current_room}. You can travel:")
    for direction, room in adjacent_rooms.items():
        print(f"Travel {direction} to visit {room}")

# You Lose...
def game_over():
    print("Sometimes my arms bend back... GAME OVER!")

# You Win!
def win_game():
    print("There they are, Albert. Faces of stone! Damn fine job! Agent Dale Cooper is safe!")

# starts the game
def main():
    clear_screen()
    introduction()
    display_controls()

 # working dictionary/key for rooms, direction of travel, and items
    rooms = {
        'The Falls': {'W': 'The Great Northern Hotel'},
        'The Great Northern Hotel': {'E': 'The Falls', 'S': 'The Double R Diner', 'Item': 'Room 315 Key'},
        'The Double R Diner': {'N': 'The Great Northern Hotel', 'W': 'The Roadhouse', 'E': 'The Owl Cave', 'S': 'The Sheriff\'s Station', 'Item': 'A Damn Fine Cup Of Coffee'},
        'The Roadhouse': {'E': 'The Double R Diner', 'Item': 'Tape Recorder'},
        'The Owl Cave': {'W': 'The Double R Diner', 'N': 'One-Eyed Jacks', 'Item': 'Mysterious Jade Signet Ring'},
        'One-Eyed Jacks': {'S': 'The Owl Cave', 'Item': 'Broken Poker Chip'},
        'The Sheriff\'s Station': {'N': 'The Double R Diner', 'E': 'The Black Lodge', 'Item': '72 Fresh Assorted Donuts'},
        'The Black Lodge': {'W': 'The Sheriff\'s Station', 'Boss': 'Bob "Heads up, tails up, run you scallywags!"'}
    }

   # starting point for room and inventory
    inventory = []
    current_room = "The Falls"
    msg = ""

# game play loop, should display current room, current inventory, and moves
    while True:
        clear_screen()
        print(f"Inventory: {inventory}\n{'-' * 27}")
        print(msg)

        # prints 'a' or 'an' accoridngly when item is seen
        if "Item" in rooms[current_room].keys():
            nearby_item = rooms[current_room]["Item"]
            indefinite_article = "an" if nearby_item[0].lower() in 'aeiou' else "a"
            print(f"You see {indefinite_article} {nearby_item}")

        #final battle, win or lose depending on inventory
        if 'Boss' in rooms[current_room].keys():
            if len(inventory) < 6:
                game_over()
                break
            else:
                win_game()
                break
        # should display current room and travel options, asks for input
        display_adjacent_rooms(current_room, rooms)
        user_input = input("Enter your move:\n").title().strip()

        # allows player to explore rooms and checks for valid input
        if user_input in ['N', 'S', 'E', 'W']:
            if user_input in rooms[current_room]:
                current_room = rooms[current_room][user_input]
                msg = f"You travel {user_input} to {current_room}."
            else:
                msg = "out of Jurisdiction."

         # inventory management, should track items collected, let them retrieve more items, and check for valid input
        elif user_input.startswith("Get "):
            item_to_get = user_input.split("Get ")[1]
            if "Item" in rooms[current_room] and item_to_get == rooms[current_room]["Item"]:
                if item_to_get not in inventory:
                    inventory.append(item_to_get)
                    msg = f"{item_to_get} retrieved!"
                else:
                    msg = f"You already have {item_to_get}."
            else:
                msg = f"Can't find {item_to_get}."

         # You Quit?!
        elif user_input == "Quit":
            break

        else:
            msg = "Invalid command"
if __name__ == "__main__":
    main()

