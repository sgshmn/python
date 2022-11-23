import sys

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-n1", "--num1")
    parser.add_argument("-n2", "--num2")
    
    args = parser.parse_args()
    
    print(args.num1)
    print(args.num2)