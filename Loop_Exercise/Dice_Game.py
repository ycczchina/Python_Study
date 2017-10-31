import random
def roll_dice(numbers=3, points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers -= 1
    return points

def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game():
    money = 1000;
    rate = 1;
    while(money > 0):
        print('<<<<< GAME STARTS! >>>>>')
        print('YOU HAVE ${} NOW !'.format(money))
        bet = int(input('Make a bet : '))
        while bet > money or bet <= 0:
            print('INVALID AMOUNT !')
            bet = int(input('Make a bet : '))
        choices = ['Big', 'Small']
        your_choice = input('Big or Small :')
        if your_choice in choices:
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if youWin:
                print('The points are',points,'You win !')
                money += bet * rate
            else:
                print('The points are',points,'You lose !')
                money -= bet * rate
                if money == 0:
                    print('YOU HAVE NO MONEY ! GAME ENDS !')
        else:
            print('Invalid Words')

start_game()
