books = ["Python", "Java", "C++", "DBMS", "Networks"]

while True:
    print("\n1.Add 2.Remove 3.Search 4.Display 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print("Book added!")

    elif choice == 2:
        book = input("Enter book name: ")
        if book in books:
            books.remove(book)
            print("Book removed!")

    elif choice == 3:
        book = input("Enter book name: ")
        print("Found!" if book in books else "Not Found!")

    elif choice == 4:
        print("Books:", books)

    elif choice == 5:
        break

    else:
        print("Invalid choice!")