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

run = True
types = restaurantData.types

RestaurantList = []
for restaurant in restaurantData.restaurant_data:
    RestaurantList.append(Restaurant(restaurant[0], restaurant[1], restaurant[2], restaurant[3], restaurant[4]))

# Style :^)
LineBreak = "\n==================================="

def search_by_letter(letter, types):
    available_types = []
    for type in types:
        if type[:len(letter)].lower() == letter.lower() and type not in available_types:
            available_types.append(type)
    return available_types

def search_by_type(type, RestaurantList):
    type_restaurants = [r for r in RestaurantList if r.type == type]
    return type_restaurants

while run:
    print("""
.-=~=-.                                                                 .-=~=-.
(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)
( _ __)                                                                 ( _ __)
(__  _)                        WELCOME TO                               (__  _)
(_ ___)                    FANTASY RESTAURANTS                          (_ ___)
(__  _)                                                                 (__  _)
(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)
`-._.-'                                                                 `-._.-'
     \n""")
    letter_search = True
    type_search = False
    while letter_search:
        print("What type of food would you like to eat?")
        letter_input = input("Search the beginning of the type of food you want to eat to see if it is available.\n")
        l_search = search_by_letter(letter_input, types)
        if len(l_search) == 0:
            print("\nSorry, we don't have any restaurants of that type.\n")
        elif len(l_search) == 1:
            print(f"\nThe only option for that search is {l_search[0]}. Would you like to search for {l_search[0]} restaurants? (y)es or (n)o\n")
            choice = input("> ")
            if choice.lower() == 'y' or choice.lower() == 'yes':
                letter_search = False
                type_search = True
                type_input = l_search[0]
            elif choice.lower() == 'n' or choice.lower() == 'no':
                pass
        else:
            print(f"\nHere are the available types of food that match your search: {l_search}.\n")
    while type_search:
        quit()
    run = False