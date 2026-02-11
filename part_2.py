def main():

    i = 0

    rover_status = {
        "Battery": 100,
        "Heater": "Off",
        "Camera": "Standby"
    }

    print(rover_status["Battery"])
    print(rover_status["Heater"])
    print(rover_status["Camera"])

    rover_status["Battery"] = 85
    rover_status["Heater"] = "On"
    rover_status["Speed"] = 5

    print(rover_status)

    Dic_1 = {
        "Site": "Crater A",
        "Radiation": "Low",
        "Water": False,
    }

    Dic_2 = {
        "Site": "Dune B",
        "Radiation": "High",
        "Water": True,
    }

    mission_log = [Dic_1, Dic_2]

    for i in range(len(mission_log)):

        dictionary = mission_log[i]
        site = dictionary["Site"]
        radiation = dictionary["Radiation"]

        print("Site: " + site + " has " + radiation + " radiation.")


main()
