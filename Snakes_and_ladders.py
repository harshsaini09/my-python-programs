import random
snakesd = {32:10,36:6,48:26,62:18,88:24,95:56,97:78}
leaderd = {1:38,4:14,8:30,21:42,28:76,50:67,71:92,80:99}
def disc():
    n = random.randint(1,6);
    return n

def snakes(score):
    count=-1
    for i in list(snakesd.keys()):
        count += 1
        if score == i:
            score = list(snakesd.values())[count]
    return score

def leadder(score):
    count=-1
    for i in list(leaderd.keys()):
        count += 1
        if score == i:
            score = list(leaderd.values())[count]
    return score

def player():
    ppl1 = 0
    ppl2 = 0
    turn = 0
    flag = 0
    name1 = input("Enter name of player 1: ")
    name2 = input("Enter name of player 2: ")
    while(flag == 0):
        if turn%2 == 0:
            print(name1," Your turn")
            c = int(input("Press 1 to continue or 0 to Quit: "))
            if(c == 0):
                print(name1," Your Score is ",ppl1)
                print(name2," Your Score is ",ppl2)
                print("game has ended!!!")
                flag = 1
            elif(c == 1):
                dics_number = disc()
                print("Dics Showed: ",dics_number)
                ppl1 += dics_number
                print(name1,"socre",ppl1)
                ppl1 = snakes(ppl1)
                ppl1 = leadder(ppl1)
                if ppl1 == 100:
                    print(name1,"wins")
                    break
                elif ppl1 >= 100:
                    ppl2 -= dics_number
            else:
                print("Wrong input!!!")
        else:
            print(name2," Your turn")
            c = int(input("Press 1 to continue or 0 to Quit: "))
            if c == 0:
                print(name1," Your Score is ",ppl1)
                print(name2," Your Score is ",ppl2)
                print("game has ended!!!")
                flag = 1
            elif(c == 1):
                dics_number = disc()
                print("Dics Showed: ",dics_number)
                ppl2 += dics_number
                print(name2,"socre",ppl2)
                ppl2 = snakes(ppl2)
                ppl2 = leadder(ppl2)
                if ppl1 == 100:
                    print(name2,"wins")
                    break
                elif ppl2 >= 100:
                    ppl2 -= dics_number
            else:
                print("Wrong input!!!")
        turn+=1     
player()