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