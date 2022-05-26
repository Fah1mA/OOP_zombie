from room import Room
from character import Character, Enemy
from rgpinfo import RGPInfo

spooky_castle = RPGInfo("The spooky castle")
spooky_castle.welcome()
RPGInfo.info()

RPGInfo.author = "Raspberry Pi Foundation"
RPGInfo.credits()

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dininghall = Room("Dining Hall")

kitchen.set_description("A dank and dirty room buzzing with flies")

dining_hall = Room("Dining hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

print("Ther are " + str(Room.number_of_rooms) + " rooms to explore.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("shotgun")
dining_hall.set_character(dave)

current_room = kitchen

dead = False

while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    
    command = input("> ")
    current_room = current_room.move(command)

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("Haha what will you use to defeat me")
            fight_with = input("What is your weapon of choice: ")
            if inhabitant.fight(fight_with) == True:
                print("Congratulations you have won the fight! ")
                current_room.set_character(None)
            else:
                print("Oh no you lost")
                print("END OF GAME")
                dead = True
        else:
            print("There is nobday here")

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I would not do that")

            else:
                inhabitant.hug()
        else:
            print("There is nobody here")

RPGInfo.credits()
