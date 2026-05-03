from main_hotel import Hotel

class Room(Hotel):
     
    def __init__(self, name, location, rooms, rating, price):
          super().__init__(name, location, rooms, rating, price)    

          self.name = name
          self.price_dict = {}
          self.rating_dict = {}

    def add_prices(self,room,price):
         self.price_dict[room] = price

    def display_prices(self):
        print(f'PriceperRoom:')
        for room, price in self.price_dict.items():
            print(f'{room}: {price}')

    def add_ratings(self,room,rating):
         self.rating_dict[room] = rating

    def display_ratings(self):
         print(f'RoomRating:')
         for room, rating in self.rating_dict.items():
              print(f'{room}: {rating}')