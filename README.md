# fire_type_with_me
Title: Fire Type With Me: A Twin Peaks text based adventure game 

OVERVIEW/GOAL
This game will require the player to navigate through rooms to collect items required to defeat a villian at the end of the game.

In order for a player to navigate in the game, develop a function/functions using Python script to do the following:
* Show the player the different commands they can enter.
* The list of navigation opens is Go North, Go South, Go East, Go West, Get Item
* Show the player’s status by identifying the room they are currently in, showing a list of their inventory of items, and displaying the item in their current room
Each step of the game will output a text prompt to let the player know where they are in the game.
Here is a sample status from the twin peaks text game:
   You are in the Great Northern Hotel
   Inventory: []
   You see a room key
   ----------------------
   Enter your move:

The gameplay loop should continue looping, allowing the player to move to different rooms and acquire items until the player has either won or lost the game. Include output to the player for both possible scenarios: winning and losing the game.

Include input validation by developing code that tells the program what to do if the player enters an invalid command.

GAME DETAILS:
Ask player to enter thier last name:

Print Directions for the player: Welcome to Twin Peaks Special Agent (name).
Your mission is to locate and remove Agent Dale Cooper from Twin Peaks. His exact whereabouts are unknwon we suggest you start at the Falls and trace his steps from where they found her wrapped in plastic. 

You must enter North, South, East, or West to move around town 

We belive Agent Cooper may have left notes or perosnal belonings throughout the area as well, please keep an eye out and enter "get item" to collect these artifacts.

The locations are as follows: 
The Falls (game entrance, no item)
The Great Northern Hotel
The Double R Diner
The Roadhouse
One-Eyed Jacks
Sheriffs Station
Owl Cave
The Black Lodge (Villain loacted here, no itemn, but when the player is in this room text will print backwards)

The items are as follows: 
315 Room Key "CLEAN PLACE REASONABLY PRICED" (located in The Great Northern Hotel)
A Damn Fine Cup of Coffee (located in The Double R Diner)
Tape Recorder "Diane..." (located in The Roadhouse)
Broken Poker Chip (located in One-Eyed Jacks)
72 Fresh Assorted donuts (located in the Sheriffs Station)
Mysterious Jade Signet Ring (located in the Owl Cave)

The Black Lodge is where Bob is keeping Cooper. 

Enter The Black Lodge with all items to save Coop, in this sceanrio print "There they are, Albert. Faces of stone! Good job, Agent Dale Cooper is safe"

 Enter without all of the items and remain trapped with cooper for eternity, in this scenario print  "Sometimes my arms bend back" "GAME OVER"