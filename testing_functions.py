"""
Project: Discordgg.py
File: testing_functions.py
Author: @Daniel Chung
Date: 10/12/19
Description: This file contains all the functions that are
for testing.
Installs: Discord.py
"""

from discordgg import *

def test_getWinRatio():
    print("** TESTING getWinRatio(wins, loses) **")
    hundred = getWinRatio(100, 0)
    fifty = getWinRatio(100, 100)
    zero = getWinRatio(0, 100)
    print(hundred == 100)
    print(fifty == 50)
    print(zero == 0)

"""
Testing function to test if the cross server works.
"""
def test_getRegion():
    print("** TESTING getRegion(message) **")
    test1 = "!na pikachung"
    test2 = "!euw pikachung"
    test3 = "!lan pikachung"
    test4 = "!las pikachung"
    print(getRegion(test1) == "na1")
    print(getRegion(test2) == "euw1")
    print(getRegion(test3) == "la1")
    print(getRegion(test4) == "la2")

def main():
    test_getWinRatio()
    test_getRegion()

if __name__ == '__main__':
    main()