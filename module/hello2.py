# hello2.py
import sys

def printHello(s):
    if s == "1":
        print("Hello")
    else:
        print("!")
    
if __name__ == "__main__":
    # 외부 매개변수를 받는다
    
    printHello(sys.argv[1])