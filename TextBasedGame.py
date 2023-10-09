import os

#clears terminal
def clear():
    os.system = ('cls')

#Game introuction, Asks for user to enter last name and laysout the plot + controls
name = input("Enter your last  name:")
print(f"""
Welcome to Twin Peaks, Special Agent {name}.

Your mission is to locate Special Agent Dale Cooper and remove him from Twin Peaks.
His exact where-abouts are unknown at this time, but we suggest you explore the following:

The Great Northern Hotel
The Double R diner
The Roadhouse
One-Eyed Jacks
The Sheriffs Station
The Owl Cave
The Black Lodge

""")
input ("Press any ket to continue...")

print("""
We know Special Agent Dale Cooper has left behind items in each of these locations.
It is required of you to collect these materials.
Do not enter the Black Lodge unless necessary.
Under no circumatances should you enter The Black Lodge wihtout these itmes.
""")

input("Press any key to view controls.")

print("""
ENTER: "North", "South", "East", or "West" to move beteween rooms
ENTER: "Get Item" to pick up items.

Remember, the owls are not what they seem...
""")

#starts game
input("Press any key to enter Twin Peaks...")

#Room Navigation
rooms ={
    'The Falls' : {'West' : 'The Great Northern Hotel'},
    'The Great Northern Hotel' : {'East' : 'The Falls', 'South' : 'The Double R Diner', 'Item' : 'Room 315 key "clean place reasonably priced"' }, 
    'The Double R Diner' : {'North' : 'The Great Northern Hotel', 'West' : 'The Roadhouse', 'East' : 'The Owl Cave', 'South' : 'The Sheriffs Station', 'Item' : 'A Damn Fine Cup of Coffee'},
    'The Roadhouse' : {'East': 'The Double R Diner', 'Item' : 'Tape Recorder "Diane..."'},
    'The Owl Cave' : {'West' : 'Double R Diner', 'North' : 'One-Eyed Jacks', 'Item' : 'Mysterious Jade Signet Ring'},
    'One-Eyed Jacks' : {'South' : 'The Owl Cave', 'Item' : 'Broken Poker Chip'},
    'The Sheriffs Station' : {'North' : 'The Double R Diner', 'East' : 'The Black Lodge', 'Item' : '72 Fresh Assorted donuts'},
    'The Black Lodge' : {'West' : 'The Sheriffs Station', 'Boss' : 'Bob "Heads up, tails up, run you scallywags. Night falls, morning calls, Ill catch you with my death bag. You may think Ive gone insane, but I promise, I will kill again!"'}
}

#list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

#track inventory
inventory = []

#track current room
current_room = "The Falls"

#result of last move
msg = ""

#clears terminal
clear()

#Gameplay loop (represents players turn)
while True:

    clear() 
    #Displays info for player
    print(f"Welcomt to {current_room}\nInventory : {inventory}\n '-' * 27 ")

    #Displays msg
    print(msg)

    #item indictaor
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:

            # plural
            if nearby_item[-1] == 's' :
                print(f"You see {nearby_item}")
            
            # Singular starts with vowel
            elif nearby_item[0] in vowels:
                print (f"You see an{nearby_item}")
            
            # Singular starts with consanant
            else:
                print(f"You see a {nearby_item}")
    #Boss encounter
    if 'Boss' in rooms[current_room].keys():

        #You Lose...
        if len(inventory) < 6:
            print("Sometimes my arms bend back... GAME OVER!")
            break

        #You Win!
        else:
            print("There they are, Albert. Faces of stone! Damn fine job! Agent Dale Cooper is safe!")
            break

# Accepts players moves as input
user_input = input("Enter your move:\n")

#splits move into words
next_move = user_input.split(' ')

#first word is action
action = next_move[0].title()

if len(next_move) > 1:
    item = next_move [1:]
    direction = next_move[1].title()

    item = ' '.join(item).title()

#moving between rooms
if action == 'Go':

    try:
        current_room = rooms[current_room][direction]
        msg = f"You travel {direction}."

    except:
        msg = f"Out of jurisdiction"

#Get item
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

#Exit the game
elif action == "Exit":
        break

#Any other commands invalid
else:
    msg = "Invalid command"