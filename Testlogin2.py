#Python test login and register w classes (NEA)


import random
import time
    

class USERS:
    def create(self):
        username = input("Pls enter a usn: ")
        password = input("Pls enter a pswd: ")
        logform = "{u}:{p}".format(u = username, p = password)
        with open("accountsfile.txt", "a") as f:
            line = logform + "\n"
            f.write(line)
            f.close()
            print("great, now login:")


            
    def login(self):
        f = open("accountsfile.txt", "r")
        usn = input("Enter a usn: ")
        pswd = input("Enter a pswd: ")
        logform2 = "{u1}:{p1}".format(u1 = usn, p1 = pswd) + "\n"
        line = f.readline()
        for line in f:
            if line == logform2 and len(line) == len(logform2):
                print("great, now loading dicegame: ")
                return(usn,pswd)
                break
        if not(line == logform2 and len(line) == len(logform2)):
            print("incorrect")
            exit()

            
    def dicegame(self):
        score = 0
        i = 0
        turns = 5
        while i < turns:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            result = dice1 + dice2 
            print(dice1,dice2)
            print(result)
            if result % 2 == 0:
                score += 10
                if dice1 == dice2:
                    turns += 1
            elif not(result % 2 == 0):
                if score > 0 :
                    score = score -5
                else:
                    score = 0
            i += 1
        time.sleep(0.5)    
        print(score)
        return(score)

    

    
    def choose(self):
        ans1 = input("do you want to create 2 new accounts or just login? 'c' = create. 'l' = login: ")
        if ans1 == 'c':
            print("user1:")
            USERS().create()
            user1,pass1 = USERS().login()
            print("user 1: " , user1)
            score1 = USERS().dicegame()
            print("now user 2:")
            USERS().create()
            user2,pass2 = USERS().login()
            print("user 1: " , user2)
            score2 = USERS().dicegame()
        elif ans1 == 'l':
            print("user 1:")
            user1,pass1 = USERS().login()
            score1 = USERS().dicegame()
            print("now user 2:")
            user2,pass2 = USERS().login()
            score2 = USERS().dicegame()
        
        if score1 > score2:
            u1 = USERS().uwin(user1,pass1,score1)
            u1()
        elif score1 < score2:
            u2 = USERS().uwin(user2,pass2,score2)
            u2()
        else:
            print("draw!!!!")
            user1di , user2di = USERS().draw()
            if user1di > user2di:
                score1 += 10
                u1 = USERS().uwin(user1,pass1,score1)
                
            elif user1di < user2di:
                score2 += 10
                u2 = USERS().uwin(user2,pass2,score2)
                
    def uwin(self,user,pasw,score):
        w = open("winners.txt", "a")
        print(user, " wins!")
        form = "{u}:{p}:{s}".format(u = user, p = pasw, s = score) + "\n"
        w.write(form)
        w.close()


    def draw(self):
        x = True
        while x == True:
            u1dice = random.randint(1,6)
            print("u1:" , u1dice)
            u2dice = random.randint(1,6)
            print("u2:" , u2dice)
            if u1dice != u2dice:
                x = False
        return u1dice , u2dice

USERS().choose()






    


