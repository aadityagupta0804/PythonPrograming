import unittest


class CredentialCheck(unittest.TestCase):

    def writeFile(self, username=None, password=None):
        logform = "{u}:{p}".format(u=username, p=password)
        with open("Test.txt", "a") as myfile:
            myfile.write(logform)

    def readFile(self):
        f = open("Test.txt", "r")
        readerList = []
        for x in f:
            print(x)
            readerList.append(x)

        username_try = input("user: ")
        password_try = input("pss: ")
        logform2 = "{u1}:{p1}".format(u1=username_try, p1=password_try)
        for line in readerList:
            if line == logform2 and len(line) == len(logform2):
                print("great")
                break

    def test_credential(self):
        print("enter a new user: ")
        username = input()
        print("new password: ")
        password = input()
        self.writeFile(username=username, password=password)
        self.readFile()


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
