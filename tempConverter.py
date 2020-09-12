#!/usr/bin/env python3
# Author: Mark Kaiser
# Date: 04/09/2020
# Description: A temperature converter.
import argparse

def celsius(f):
    ''' calculates celsius with user provided fahrenheit temperature. celsius() takes a float or int'''
    c = (5/9 * (f - 32))
    print(f"{f} degrees fahrenheit is equal to {c.__round__(1)} degrees celsius")

def fahrenheit(c):
    ''' calculates fahrenheit with user provided celsius temperature. fahrenheit() takes a float or int'''
    f = ((9/5 * c) + 32)
    print(f"{c} degrees celsius is equal to {f.__round__(1)} degrees fahrenheit")

#argument parser to construct help menu and handle user supplied values
def main():
    ''' This is the main function for temp converter'''
    #argparse to build help menu and handle user supplied parameter values
    parser = argparse.ArgumentParser(description='Convert celsius to fahrenheit or vice versa')
    parser.add_argument('-f', '--fahrenheit', dest='fahrenheit', type=float, required=False, help='provide a temperature in fahrenheit')
    parser.add_argument('-v', '--version', dest='ver', required=False, action='store_true', help='display program version number.')
    parser.add_argument('-c', '--celsius', dest='celsius', required=False, type=float, help="provide a temperature in celsius")
    args = parser.parse_args()

    #determines if -f value supplied and calls fahrenheit function if calculations required
    if args.fahrenheit:
        fahrenheit(args.fahrenheit)
    elif args.fahrenheit == 0:
        print("32 degrees fahrenheit is equal to 0 degrees celsius")

    #determines if -c value supplied and calls celsius function if calculations required
    if args.celsius:
        celsius(args.celsius)
    elif args.celsius == 0:
        print("0 degrees celsius is equal to 32 degrees fahrenheit")
    
    #determines if -v used and provides program version information
    if args.ver:
        print("temp converter version 0.2")
        exit()

if __name__ == '__main__':
    main()
