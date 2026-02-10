def main():

    sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
    new_findings = []
    counter = 0
    i = 0

    print(sample_bay[0])
    print(sample_bay[len(sample_bay) - 1])
    print(len(sample_bay))

    for _ in range(len(sample_bay)):
        print("Transmitting data for: " + sample_bay[_])

    while counter < 3:
        new = input("What is the new rock?")
        new_findings.append(new)
        counter += 1
    
    print(new_findings)

    sample_bay.remove("Dust")
    print(sample_bay)

main()
