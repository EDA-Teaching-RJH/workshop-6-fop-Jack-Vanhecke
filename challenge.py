def main():

    i = 0
    rover_state = {"x": 0, "y": 0, "samples": 0}
    command_batch = ["MOVE 10", "TURN LEFT", "MOVE 5", "MOVE five", 'five', "DIG", "MOVE 20", "XÆA-12", "RETURN", "MOVE 15"]

    for i in range(len(command_batch)):
        command = command_batch[i]
        split_command = command.split()

        if split_command[0] == "MOVE":
            action = split_command[1]

            try:
                action = int(action)
                rover_state["y"] += action
            except ValueError:
                print("Invalid. Distance Ignored")
                i += 1

        elif split_command[0] == "DIG":
            rover_state["samples"] += 1

        elif split_command[0] == "TURN":
            print("Turning...")

        else:
            print("Error: Unknown command sequence")
    
    print(rover_state)

main()
