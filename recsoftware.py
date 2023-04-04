import restaurantData


class Restaurant:
    def __init__(self, type, name, price, rating, address):
        self.type = type
        self.name = name
        self.price = price
        self.rating = rating
        self.address = address
    
    def __repr__(self):
        return f'\n{self.name}\n{self.rating}/5 stars\n{self.price}\nAddress: {self.address}'

types = restaurantData.types

RestaurantList = []
for restaurant in restaurantData.restaurant_data:
    RestaurantList.append(Restaurant(restaurant[0], restaurant[1], restaurant[2], restaurant[3], restaurant[4]))

# Style :^)
LineBreak = "\n==================================="

def search_by_letter(letter, types):
    available_types = []
