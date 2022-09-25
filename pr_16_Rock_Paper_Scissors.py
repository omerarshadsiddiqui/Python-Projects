import random

def gameWin(comp,user):
    if comp == user:
        return None
    if comp == 'r':
        if user == 'p':
            return True
        elif user == 's':
            return False
    elif comp == 'p':
        if user == 's':
            return True
        elif user == 'r':
            return False
    elif comp == 's':
        if user == 'r':
            return True
        elif user == 'p':
            return False

comp = print("Computer will choose, Select Rock(r) , Paper(p) , Scissors(s) \n")
randno = random.randint(1,3)
if randno == 1:
    comp == 'r'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 's'

user = input("Hello User, Select Rock(r) , Paper(p) , Scissors(s)\n")
a = gameWin(comp,user)

print(f"Computer choose {comp}")
print(f"User choose {user}")

if a == None:
    print('its a tie')
elif  a:
    print('You win')
else: 
    print('You loose')