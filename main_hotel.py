class Hotel:
     def __init__(self,name,location,rooms,rating
                  ,price):
          self.name = name
          self.location = location
          self.rooms = rooms
          self.rating = rating
          self.price = price


     def display_hotel_info(self):
       
        print(f'Name: {self.name}')
        print(f'Location: {self.location}')
        print(f'RoomsAvailable: {self.rooms}')
        print(f'RoomRating: {self.rating}')
        print(f'PriceperRoom: {self.price}')