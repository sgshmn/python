from random import randint              
def exNum():
    n1 = int(input("처음 >> "))
    n2 = int(input(" 끝  >> "))
    print()
    return randint(n1, n2)

def inNum():
    return int(input(" 나  >> "))

def cmpNum(myNum, ranNum):
    if myNum > ranNum:
        print("sphinx >> down")
        print()
        return True
    elif myNum < ranNum:
        print("sphinx >> up")
        print()
        return True
    else:
        print("sphinx >> 정답")
        return False