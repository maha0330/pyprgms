class Movie:
    def __init__(self, name, tickets, price):
        self.name = name
        self.tickets = tickets
        self.price = price

    def display(self):
        print("Movie:", self.name)
        print("Tickets:", self.tickets)
        print("Price per Ticket:", self.price)

    def total(self):
        print("Total Amount:", self.tickets * self.price)


movie1 = Movie("Leo", 3, 200)

movie1.display()
movie1.total()