#!/usr/bin/env python3
# coding=UTF-8
import sys
import os

def google(search,bowser):
    if search.find(" ") > -1:
        search = search.replace(" ", "+")
    url = 'https://google.com/search?q=' + search
    os.system("open -a " + bowser + " " + url)

if __name__ == "__main__":
    if sys.argv[1] == '-h' or len(sys.argv) < 1:
        print('Usage: google <The things you want to search> <bowser(default is Google Chrome)>')
        sys.exit()
    elif len(sys.argv) < 3:
        google(sys.argv[1],'Google\ Chrome')
    else:
        google(sys.argv[1],sys.argv[2])