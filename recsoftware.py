import restaurantData


class Restaurant:
    def __init__(self, cuisine, name, price, rating, address):
        self.cuisine = cuisine
        self.name = name
        self.price = price
        self.rating = rating
        self.address = address
    
    def __repr__(self):
        return f'\n{self.name}\n{self.rating} stars\n{self.price}\nAddress: {self.address}'
    
RestaurantList = []
LineBreak = "\n==================================="
for restaurant in restaurantData.restaurant_data:
    RestaurantList.append(Restaurant(restaurant[0], restaurant[1], restaurant[3], restaurant[2], restaurant[4]))

for rest in RestaurantList:
    print(LineBreak)
    print(rest)
print(LineBreak)