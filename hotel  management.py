class Hotel:
    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms

    def display_info(self):
        print(f"Hotel Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Number of Rooms: {self.rooms}")

hotel1 = Hotel('Grand Hotel', 'New York', 100)
hotel1.display_info()

hotel2 = Hotel('Beach Resort', 'Miami', 50)
hotel2.display_info()

def display_hotels(hotels):
    for hotel in hotels:
        hotel.display_info()
        print()

hotels = [hotel1, hotel2]
display_hotels(hotels)  
