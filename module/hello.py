# hello.py

def printHello():
    print(__name__)
    print("Hello")
    
# __name__ : 모듈의 이름
# __main__ : 모듈을 직접 실행하면 가지는 이름
# 모듈을 직접 실행 했다면 아래를 실행한다
if __name__ == "__main__":
    print("모듈을 직접 실행")
    printHello()