print("\n Even and Odd Numbers")
for i in range(1, 6):
    for j in range(1, 6):
        number = (i - 1) * 5 + j

        if number % 2 == 0:
            print(number, "Even", end=" | ")
        else:
            print(number, "Odd", end=" | ")

    print()
