print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')


print('You are at a cross road. Where do you want to go?')
left_or_right = input('Type "left" or "right" ').lower()

if left_or_right == 'left':
    print('You have come to a lake. There is an island in the middle of the lake.')
    wait_or_swim = input('Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if wait_or_swim == 'wait':
        print('You are in front of a cave. Do You want to enter the cave or walk away?')
        enter_or_leave = input('Type "enter" or "away".').lower()
        if enter_or_leave == 'enter':
            print('Congratulations You have found the treasure! You Won!')
        else:
            print('You lose.')
    else:
        print('Lake was to big. You did not make it. You lose.')
else:
    print('You have come to the end of the road. You lose.')


