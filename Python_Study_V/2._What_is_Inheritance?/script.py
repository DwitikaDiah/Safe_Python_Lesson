from menu_item import MenuItem
from food import Food
from drink import Drink

food1 = Food('Sandwich', 5, 330)
food2 = Food('Chocolate Cake', 4, 450)
food3 = Food('Sus Cake', 2, 180)

foods = [food1, food2, food3]

drink1 = Drink('Coffee', 3, 180)
drink2 = Drink('Orange Juice', 2, 350)
drink3 = Drink('Espresso', 3, 30)

drinks = [drink1, drink2, drink3]

print('Food')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Drink')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')
order = int(input('Input food number: '))
selected_food = foods[order]
print('Selected food: ' + selected_food.name)

order = int(input('Input drink number: '))
selected_drink = drinks[order]
print('Selected drink: ' + selected_drink.name)

count = int(input('Enter quantity (10% off for 3 or more): '))
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)
print('Your total is $'  + str(result))