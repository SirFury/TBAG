from room import Room # or just import romm if we wanted to import the whole file and not just the class Room
from character import Enemy, Frenemy, Friend


kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom.set_description("A vast room with a shiny floor.")
dining_hall.set_description("An ornate room with tables and chairs.")

print(kitchen.get_description())
# print(ballroom.get_description())
# print(dining_hall.get_description())

# or (due to def describe(self) in main.py)
# kitchen.describe()
# ballroom.describe()
# dining_hall.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

aaron = Friend("Aaron", "The Game Master!")
aaron.set_conversation("Do you have your assignment?")
aaron.set_weakness("tbag")
kitchen.set_character(aaron)

dave = Enemy("Dave", "A smelly zombie.")
dave.set_conversation("Braiiiiiiiiiiins!")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

dracula = Frenemy("Dracula", "Lord of the vampires!")
dracula.set_conversation("Give me your blood or dieeeeeeeee!")
dracula.set_weakness("blood")
ballroom.set_character(dracula)



# dining_hall.get_details()
# kitchen.get_details()
# ballroom.get_details()


# The main gameplay loop

current_room = kitchen
while True:
    print("\n") # output in new line
    current_room.get_details()
    inhabitant = current_room.get_character()
    if  inhabitant is not None:
        inhabitant.describe()
        inhabitant.talk()
        user_item = input("What will you use?")
        inhabitant.interact(user_item)
        if user_item == 'cheese':
            True
        elif user_item == 'tbag':
            True
        elif user_item == 'blood':
            True
        else:
            False
        

  
    command = input(">")
    
 # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

        


