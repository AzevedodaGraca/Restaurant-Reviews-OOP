from models.restaurant import Restaurant

square_restaurant = Restaurant('praça', 'Gourmet')
square_restaurant.receive_review('Gui', 10)
square_restaurant.receive_review('Lais', 8)
square_restaurant.receive_review('Emy', 2)

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()
