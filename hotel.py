class Hotel:
    sortParam = 'name'  
    def __init__(self) -> None:
        self.name = ''
        self.location = ''
        self.rooms = 0
        self.rating = int
        self.pricePr = 0.0

        def __lt__(self,other):
            getattr(self,Hotel.sortParam) < getattr(other,Hotel.sortParam)
            
            #function to change sort parameter to name, location, rooms, rating or pricePr
            @classmethod
            def sortByName(cls):
                cls.sortParam = 'name'
            #function to change sort parameter to name, location, rooms, rating or pricePr

            @classmethod
            def sortByRate(cls):
                cls.sortParam = 'rating'


            @classmethod
            def sortByPrice(cls):
                cls.sortParam = 'pricePr'


            @classmethod
            def sortByRoomAvailability(cls):
                cls.sortParam = 'rooms'


            def __repr__(self) -> str:
                return f"Hotel(name={self.name}, location={self.location}, rooms={self.rooms}, rating={self.rating}, pricePr={self.pricePr})"   
            
    #class for user data
class User:
    def __init__(self) -> None:
        self.name = ''
        self.uId = 0
        self.cost = 0.0

        def __repr__(self) -> str:
            return f"User(name={self.name}, uId={self.uId}, cost={self.cost})"
        
        #print hotel data
    def printHotelData(hotels):
      for h in hotels:
        print(h)
    #sort hotels by name
    def sortHotelsByName(hotels):
        print("Sorting hotels by name...")

        Hotel.sortByName()
        hotels.sort()

        printHotelData(hotels)
        print()
        return sorted(hotels)
    #sort hotels by rating
    def sortHotelsByRating(hotels):
        print("Sorting hotels by rating...")

        Hotel.sortByRate()
        hotels.sort()

        printHotelData(hotels)
        print()
        return sorted(hotels)
    
    #sort hotels by price    
    def sortHotelsByPrice(hotels):
        print("Sorting hotels by price...")     

        Hotel.sortByPrice()
        hotels.sort()

        printHotelData(hotels)
        print()
        return sorted(hotels)
    
    #sort hotels by room availability
    def sortHotelsByRoomAvailability(hotels):
        print("Sorting hotels by room availability...")

        Hotel.sortByRoomAvailability()
        hotels.sort()

        printHotelData(hotels)
        print()
        return sorted(hotels)
    
    #print user data
    def printUserData(userName, userId, bookingCost, hotels):
        users = []
         #accessuser data and print it

        
        for  i in range(3):
            user = User()
            user.name = userName[i]
            user.uId = userId[i]
            user.cost = bookingCost[i]
            users.append(user)
    
        for u in users:
            print(u)


    #function to solve Hotel Management problem
    def solveHotelManagement( userName, userId, bookingCost,rooms,locations ,ratings,prices):
        #initialize array that stores hotel data and user data
        hotels = []
         #crete objects for hotel and user
          
        for i in range(3):
            hotel = Hotel()
            hotel.name = f"Hotel {i+1}"
            hotel.location = locations[i]
            hotel.rooms = rooms[i]
            hotel.rating = ratings[i]
            hotel.pricePr = prices[i]
            hotels.append(hotel)

        print("Hotel Data:")
        printHotelData(hotels)
        print()


        #call the various operatons on hotel data and user data
        sortHotelsByName(hotels)
        sortHotelsByRating(hotels)
        sortHotelsByPrice(hotels)
        sortHotelsByRoomAvailability(hotels)
        print("User Data:")
        printUserData(userName, userId, bookingCost, hotels)

        #driver code to test the function
if __name__ == "__main__":
    userName = ['Alice', 'Bob', 'Charlie']
    userId = [1, 2, 3]
    bookingCost = [200.0, 150.0, 300.0]
    rooms = [10, 20, 5]
    locations = ['New York', 'Miami', 'Los Angeles']
    ratings = [4.5, 4.0, 4.8]
    prices = [100.0, 80.0, 120.0]

   # solveHotelManagement(userName, userId, bookingCost, rooms, locations, ratings, prices)

    #function to perform operations
    #def HotelManagement(userName, userId, bookingCost, rooms, locations, ratings, prices):
                  