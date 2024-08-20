def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

destination = input("Where do you want to go?")

start_engine()            
move_forward()

if destination == "library":
    move_forward()
    turn("left")
    print("We arrived at library!")

elif destination == "tech park":
    move_forward()
    turn("right")
    print("We arrived at tech park")

elif destination == "hospital" or destination == "mall" or destination == "airport" or destination == "university" or destination == "stadium":
    move_forward()
    if destination == "hospital":
        follow_roundabout(1)
        stop_engine()
    elif destination == "mall":
        follow_roundabout(2)
        stop_engine()
    elif destination == "airport":
        follow_roundabout(3)
        stop_engine()
    elif destination == "university":
        follow_roundabout(4)
        turn("left")
        stop_engine()
    elif destination == "stadium":
        follow_roundabout(4)
        move_forward()
        turn("right")
        stop_engine()

else: 
    print("Stop the engine.")