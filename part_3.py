def get_coordinate():
    while True:
        try:
            x_coord = int(input("What is the x-coordinate? "))

            if -100 <= x_coord <= 100:
                return(x_coord)
                break
            else:
                print("Coordinate out of range.")
                
        except ValueError:
            print("Invalid coordinate.")

def main():

    try:
        speed = int(input("Enter motor speed. "))
        print("Speed set to: " + str(speed))
    except ValueError:
        print("Error: Corrupted signal. Maintaining current speed.")
    
    print(str(get_coordinate()))

main()
