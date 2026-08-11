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
        total_amount=self.tickets*self.price
        print("Total Amount:",total_amount)
name=input("enter movie name:")
tickets=int(input("enter number of tickets:"))
price=200
movie1=Movie(name,tickets,price)
movie1.display()
movie1.total()