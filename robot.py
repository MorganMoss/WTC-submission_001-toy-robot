
def move_forward(distance):
    """
    The robot will move forward by the distance specified
    """
    print(f"* Move Forward {distance}")


def turn_right(degrees):
    """
    The robot will turn right by the amount
    of degrees specified
    """
    print(f"* Turn Right {degrees} degrees")


def move_square(size):
    """
    size decides the distance the robot will go
    for each side of the square
    """
    move_rectangle(size, size)
    

def move_rectangle(length, width):
    """
    length and width decide the distance the robot will go
    for the two sides of the rectangle. If they are equal,
    they will move in a square 
    """
    if length != width:
        print(f"Moving in a rectangle of {length} by {width}")
    else:
        print(f"Moving in a square of size {length}")
    degrees = 90
    for i in range(2):
        move_forward(length)
        turn_right(degrees)
        move_forward(width)
        turn_right(degrees)


def move_circle(length = 1):
    """
    The robot moves in a circle with a circumference
    of length multiplied by 360. By default length = 1
    """
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        move_forward(length)
        turn_right(degrees)


def move_square_dancing(length):
    """
    Will move forward and move in a square, repeat 3 times
    length decides the size of the square and the distance
    it will move forward
    """
    print(f"Square dancing - 3 squares of size {length}")
    for i in range(3):
        move_forward(length)
        move_square(length)


def move_crop_circles(length):
    """
    Will move forward and move in a circle, repeat 4 times
    length decides how far it moves forward
    """
    print("Crop circles - 4 circles")
    for i in range(4):
        move_forward(length)
        move_circle()


def move():
    """
    This Goes through each preprogrammed 
    movement pattern available to the 
    robot.
    """
    move_square(size = 10)
    move_rectangle(length = 20, width = 10)
    move_circle()
    move_square_dancing(length = 20)
    move_crop_circles(length = 20)


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
