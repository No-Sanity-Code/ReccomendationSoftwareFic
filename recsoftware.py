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
# Chose nested while loops for smoother input handling
while run:
    letter_search = True
    type_input = ''
    while letter_search:
        print("What type of food would you like to eat?")
        letter_input = input("Search the beginning of the type of food you want to eat to see if it is available.\n")
        l_search = search_by_letter(letter_input, types)
        if len(l_search) == 0:
            print("\nSorry, we don't have any restaurants of that type.\n")
        elif len(l_search) == 1:
            print(f"\nThe only option for that search is {l_search[0]}. Would you like to search for {l_search[0]} restaurants? (y)es or (n)o")
            choice = input("> ")
            if choice.lower() == 'y' or choice.lower() == 'yes':                
                type_input = l_search[0]
                letter_search = False
            elif choice.lower() == 'n' or choice.lower() == 'no':
                pass
        else:
            print(f"\nHere are the available types of food that match your search: {l_search}.\n")
    sort_choice = input("\nWould you like to sort by (p)rice, (r)ating, or (n)ame?\n> ")
    if sort_choice.lower() == 'p' or sort_choice.lower() == 'price':
        type_choice_list = search_by_type(type_input, RestaurantList)
        sort_list = sorted(type_choice_list, key=lambda r: r.price)
        for restaurant in sort_list:
          print(LineBreak)
          print(restaurant)
        print(LineBreak)
        loop_input = input("\nWould you like to search again? (y)es or (n)o\n> ")
        if loop_input.lower() == 'y' or loop_input.lower() == 'yes':
            letter_search = True
        elif loop_input.lower() == 'n' or loop_input.lower() == 'no':
            run = False
    elif sort_choice.lower() == 'r' or sort_choice.lower() == 'rating':
        type_choice_list = search_by_type(type_input, RestaurantList)
        sort_list = sorted(type_choice_list, key=lambda r: r.rating, reverse=True)
        for restaurant in sort_list:
          print(LineBreak)
          print(restaurant)
        print(LineBreak)
        loop_input = input("\nWould you like to search again? (y)es or (n)o\n> ")
        if loop_input.lower() == 'y' or loop_input.lower() == 'yes':
            letter_search = True
        elif loop_input.lower() == 'n' or loop_input.lower() == 'no':
            run = False
    elif sort_choice.lower() == 'n' or sort_choice.lower() == 'name':
        type_choice_list = search_by_type(type_input, RestaurantList)
        sort_list = sorted(type_choice_list, key=lambda r: r.name)
        for restaurant in sort_list:
          print(LineBreak)
          print(restaurant)
        print(LineBreak)
        loop_input = input("\nWould you like to search again? (y)es or (n)o\n> ")
        if loop_input.lower() == 'y' or loop_input.lower() == 'yes':
            letter_search = True
        elif loop_input.lower() == 'n' or loop_input.lower() == 'no':
            run = False
    else:
        print("\nInvalid input. Sorting by name.\n")
        type_choice_list = search_by_type(type_input, RestaurantList)
        sort_list = sorted(type_choice_list, key=lambda r: r.name)
        for restaurant in sort_list:
          print(LineBreak)
          print(restaurant)
        print(LineBreak)
        loop_input = input("\nWould you like to search again? (y)es or (n)o\n> ")
        if loop_input.lower() == 'y' or loop_input.lower() == 'yes':
            letter_search = True
        elif loop_input.lower() == 'n' or loop_input.lower() == 'no':
            run = False