class Hotel:
    def __init__(self, name, days, price):
        self.name = name
        self.days = days
        self.price = price

    def display(self):
        print("\nBooking Details")
        print("Customer:", self.name)
        print("Days:", self.days)
        print("Price per Day:", self.price)

    def total(self):
        total = self.days * self.price
        print("Total Amount:", total)


name = input("Enter customer name: ")
days = int(input("Enter number of days: "))
price = float(input("Enter price per day: "))

hotel1 = Hotel(name, days, price)

hotel1.display()
hotel1.total()