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
    'The Great Northern Hotel' : {'East' : 'The Falls', 'South' : 'The Double R Diner'}, 
    'The Double R Diner' : {'North' : 'The Great Northern Hotel', 'West' : 'The Roadhouse', 'East' : 'The Owl Cave', 'South' : 'The Sheriffs Station'},
    'The Roadhouse' : {'East': 'The Double R Diner'},
    'The Owl Cave' : {'West' : 'Double R Diner', 'North' : 'One-Eyed Jacks'},
    'One-Eyed Jacks' : {'South' : 'The Owl Cave'},
    'The Sheriffs Station' : {'North' : 'The Double R Diner', 'East' : 'The Black Lodge'},
    'The Black Lodge' : {'West' : 'The Sheriffs Station'}
}