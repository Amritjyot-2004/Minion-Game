while True:
    u=int(input('''
    1=Start
    2=Exit
    '''))
    if u==1:
        pass
    elif u==2:
        break
    else:
        print("Invalid input")
        break
    Player_1=input("Enter first player's name: ")
    Player_2=input("Enter second player's name: ")
    def minion_game(string):
        P1=0
        P2=0
        for i in range(len(string)):
            if string[i] not in 'AEIOU':
                P1+=len(string)-i
            else:
                P2+=len(string)-i
        if P1>P2:
            print(Player_1,"wins the game with",P1,"points")
        elif P2>P1:
            print(Player_2,"wins the game with",P2,"points")
        else:
            print("The game Draws")
    s=input("Enter the string: ")
    print(minion_game(s))