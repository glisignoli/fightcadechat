import threading
import sys
from time import sleep

class testThread():
    counter = 0

    def __init__(self):
        counter = 0
    
    def incrementCounter(self):
        self.counter += 1

    def printCounter(self):
        print(f'{self.counter}')

    def sleepMe(self):
        sleep(1)

    def mainIncrement(self):
        while True:
            self.incrementCounter()
            self.sleepMe()

    def mainPrint(self):
        while True:
            self.printCounter()
            self.sleepMe()

def main():
    # Create object
    myTest = testThread()
    
    # Add object to thread
    t = threading.Thread(target=myTest.mainIncrement)
    tt = threading.Thread(target=myTest.mainPrint)
    t.start()
    tt.start()

    while True:
        # Manipulate running thread
        modifier = input('Enter a modifier (+,-)')
        number = input('Enter a number (int):')
        if modifier.rstrip() is '+':
            myTest.counter += int(number)
        if modifier.rstrip() is '-':
            myTest.counter -= int(number)
        if modifier.rstrip() == 'exit':
            sys.exit()
        print(f'Printing counter {myTest.counter}')

if __name__ == '__main__':
    main()
