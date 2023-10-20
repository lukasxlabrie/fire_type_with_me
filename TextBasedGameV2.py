import os

# keeps terminal clean for mac or pc
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
        else:
        os.system('clear')

# Game introduction, prompts user for last name and sets the stage with a Twin Peaks twist
name = input("Enter your last name: ")
print(f"""
Welcome to Twin Peaks, Special Agent {name}.

Your mission: find Special Agent Dale Cooper and escort him out of Twin Peaks.
His exact location is unknown, but we recommend investigating the following places:

The Great Northern Hotel
The Double R Diner
The Roadhouse
One-Eyed Jacks
The Sheriff's Station
The Owl Cave
The Black Lodge

""")
input("Press Enter to continue...")

print("""
We suspect Special Agent Dale Cooper has left crucial items in each location.
Your task is to collect these materials.
Avoid the Black Lodge unless absolutely necessary.
Do not enter without these items.

""")
input("Press Enter to view controls.")

print("""
ENTER: "North", "South", "East", or "West" to move between rooms.
ENTER: "Get Item" to pick up items.

Remember, the owls are not what they seem...
""")

# Game begins
input("Press Enter to enter Twin Peaks...")

# Room Navigation
rooms = {
    'The Falls': {'West': 'The Great Northern Hotel'},
    'The Great Northern Hotel': {'East': 'The Falls', 'South': 'The Double R Diner', 'Item': 'Room 315 key "clean place reasonably priced"'}, 
    'The Double R Diner': {'North': 'The Great Northern Hotel', 'West': 'The Roadhouse', 'East': 'The Owl Cave', 'South': 'The Sheriff\'s Station', 'Item': 'A Damn Fine Cup of Coffee'},
    'The Roadhouse': {'East': 'The Double R Diner', 'Item': 'Tape Recorder "Diane..."'},
    'The Owl Cave': {'West': 'The Double R Diner', 'North': 'One-Eyed Jacks', 'Item': 'Mysterious Jade Signet Ring'},
    'One-Eyed Jacks': {'South': 'The Owl Cave', 'Item': 'Broken Poker Chip'},
    'The Sheriff\'s Station': {'North': 'The Double R Diner', 'East': 'The Black Lodge', 'Item': '72 Fresh Assorted Donuts'},
    'The Black Lodge': {'West': 'The Sheriff\'s Station', 'Boss': 'Bob "Heads up, tails up, run you scallywags. Night falls, morning calls, I\'ll catch you with my death bag. You may think I\'ve gone insane, but I promise, I will kill again!"'}
}

# Inventory tracker
inventory = []

# Current room
current_room = "The Falls"

# Last move result
msg = ""

# Clear terminal
clear_screen()

# Gameplay loop (represents player's turn)
while True:
    clear_screen() 
    # Display player info
    print(f"Welcome to {current_room}\nInventory: {inventory}\n{'-' * 27}")

    # Display message
    print(msg)

    # Item indicator
    if "Item" in rooms[current_room].keys():
        nearby_item = rooms[current_room]["Item"]
        if nearby_item not in inventory:
            # Check for vowels and display 'an' if the item starts with a vowel
            if nearby_item[0].lower() in 'aeiou':
                print(f"You see an {nearby_item}")
            else:
                print(f"You see a {nearby_item}")
                
    # Boss encounter
    if 'Boss' in rooms[current_room].keys():
        # You Lose...
        if len(inventory) < 6:
            print("Sometimes my arms bend back... GAME OVER!")
            break
        # You Win!
        else:
            print("There they are, Albert. Faces of stone! Damn fine job! Agent Dale Cooper is safe!")
            break

    # Accept player's moves as input
    user_input = input("Enter your move:\n")

    # Split move into words
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    if len(next_move) > 1:
        item = ' '.join(next_move[1:]).title()
        direction = next_move[1].title()

    # Moving between rooms
    if action == 'Go':
        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}."
        except:
            msg = f"Out of jurisdiction."

    # Get item
    elif action == 'Get':
        try:
            if item == rooms[current_room]["Item"]:
                if item not in inventory:
                    inventory.append(rooms[current_room]["Item"])
                    msg = f"{item} retrieved!"
                else:
                    msg = f"You already have the {item}."
            else:
                msg = f"Can't find {item}..."
        except:
            msg = f"Can't find {item}..."

    # Exit the game
    elif action == "Exit":
        break

    # Any other commands invalid
    else:
        msg = "Invalid command."
