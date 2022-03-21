def print_hand(hand, name='Guest'):
    print(name + ' picked: ' + hand)

print('Starting the Rock Paper Scissors game!')

# Get input, and then assign it to the player_name variable
player_name = raw_input('Please enter your name: ')
print('Name is: ' + player_name)

# Add a second argument to print_hand
print_hand('Rock', player_name)
