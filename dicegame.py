#Python test login and register w classes (NEA)
import random
import time
import unittest


class USERS(unittest.TestCase):

    def create(self):
        username = input("Pls enter a usn: ")
        password = input("Pls enter a pswd: ")
        logform = "{u}:{p}".format(u = username, p = password)
        with open("accountsfile.txt", "a") as f:
            line = logform + "\n"
            f.write(line)
            f.close()
            print("great, now login:")

        return username,password

    def login(self):
        f = open("accountsfile.txt", "r")
        readerList = []
        for x in f:
            readerList.append(x)
        usn = input("Enter a usn: ")
        pswd = input("Enter a pswd: ")
        logform2 = "{u1}:{p1}".format(u1 = usn, p1 = pswd) + "\n"
        for line in readerList:
            if line == logform2 and len(line) == len(logform2):
                print("great")
                break
        if not(line == logform2 and len(line) == len(logform2)):
            print("incorrect")
            exit()
        return usn, pswd
        

    def dicegame(self):
        print("first user 1.")
        score1 = 0
        for i in range(0,9):
            result1 = random.randint(1,6)
            score1 = score1 + result1
            print(result1)
            time.sleep(0.5)
            print(score1)
            print("now user 2.")
            score2 = 0
        for i in range(0,9):
            result2 = random.randint(1,6)
            score2 = score2 + result2
            print(result2)
            time.sleep(0.5)
            print(score2)
        if score1 > score2:
            print("user 1 wins!")
            print("end")
        elif score1 < score2:
            print("user 2 wins!")
            print("end")
        else:
            print("it was a draw!")

    def test_1(self):
        ans1 = input("do you want to create 2 new accounts or just login? 'c' = create. 'l' = login: ")
        if ans1 == 'c':
            user1,pass1 = self.create()
            print("user 1: " , user1 + ":" + pass1)
    
            user2, pass2 = self.create()
            print("now user 2:", user2 + ":" + pass2)
            print("dicegame...")
            self.dicegame()
        elif ans1 == 'l':
            user1 = self.login()
            print("user 1:", user1)
            user2 = self.login()
            print("now user 2:", user2)
            self.dicegame()
            print("dicegame...")

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
