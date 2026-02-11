def main():

    travel_log = []

    while True:
        try:
            sensor = int(input("Sensor reading (slope angle): "))

            travel_log.append(sensor)
            
            if sensor > 45:
                print("CRITICAL TILT! HALTING.")
                break

        except ValueError:

            print("Sensor Glitch.")

        print("Path Stable. Moving forward.")

    print("Mission Terminated.")
    print("Total steps taken: " + str(len((travel_log))))
    print(travel_log)
    
main()
