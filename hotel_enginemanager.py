from room import Room
import csv 
class HotelManager:
    
    def __init__(self):
        self.room = []

    def add_rooms(self):
        self.room.append(Room)
    
    def display_all_rooms(self):
       for rooms in self.room:
           Room.display_hotel_info()
           Room.display_prices()

    def load_hotels_from_csv(self,file_path):
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rooms = Room(
                    name = row['name'],
                    location = row['location'],
                    rooms = row['rooms'],
                    rating= row ['rating'],
                    price = row['price']
                    )
        self.add_rooms(Room)
                
