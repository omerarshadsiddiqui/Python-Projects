import random
Print('Dice Roll Simulator Welcomes :) \n')
repeat = True
while repeat:
    print('Rolling the dice')
    print(random.randint(1,6))
    repeat = ('y' or 'yes') in input("Type y or yes in input \n").lower()
Print('End')
