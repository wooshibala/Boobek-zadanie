def determine_position(x, y):
    current_position = [0, 0]
    current_position[0] += x
    current_position[1] += y
    return current_position

for i in range(5):
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))
    current_position = determine_position(x, y)
    print("Current position: ", current_position)