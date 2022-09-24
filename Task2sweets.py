import random
sweets = 2021
player1 = "Игрок 1"
player2 = "Игрок 2"
lottery = random.randint(1,2)
if lottery==1:
    print(f'Игрок {lottery} начинает')
    gamer1= player1
    gamer2=player2
else:
    print(f'Игрок {lottery} начинает')
    gamer1= player2
    gamer2=player1

while sweets>0:
    pl1=int(input(f'{gamer1}: Беру конфет: '))
    if pl1>28 or pl1<1:
            print("Введите количество от 1 до 28 конфет")
            pl1 = int(input("Тогда я возьму: "))
    sweets = sweets-pl1
    if sweets <=0:
        print("Ура!Победа")   

    
    if sweets>0:
        pl2 = int(input(f'{gamer2} А я возьму: '))
        if pl2>28 or pl2<1:
            print("Введите количество от 1 до 28 конфет")
            pl2 = int(input("Тогда я возьму: "))
        sweets=sweets-pl2
        
    if sweets <=0:
        print("Ура!Победа")    
