#!/usr/bin/env python3
import argparse

def celsius(f):
    ''' calculates celsius with user provided farenheit temperature. celsius() takes a float or int'''
    c = (5/9 * (f - 32))
    print(f"{f} degrees farenheit is equal to {c.__round__(1)} degrees celsius")

def farenheit(c):
    ''' calculates farenheit with user provided celsius temperature. farenheit() takes a float or int'''
    f = ((9/5 * c) + 32)
    print(f"{c} degrees celsius is equal to {f.__round__(1)} degrees farenheit")

#argument parser to construct help menu and handle user supplied values
def main():
    ''' This is the main function for temp converter'''
    #argparse to build help menu and handle user supplied parameter values
    parser = argparse.ArgumentParser(description='Convert celsius to farenheit or vice versa')
    parser.add_argument('-f', '--farenheit', dest='farenheit', type=float, required=False, help='provide a temperature in farenheit')
    parser.add_argument('-v', '--version', dest='ver', required=False, action='store_true', help='display program version number.')
    parser.add_argument('-c', '--celsius', dest='celsius', required=False, type=float, help="provide a temperature in celsius")
    args = parser.parse_args()

    #determines if -f value supplied and calls farenheit function if calculations required
    if args.farenheit:
        farenheit(args.farenheit)
    elif args.farenheit == 0:
        print("32 degrees farenheit is equal to 0 degrees celsius")

    #determines if -c value supplied and calls celsius function if calculations required
    if args.celsius:
        celsius(args.celsius)
    elif args.celsius == 0:
        print("0 degrees celsius is equal to 32 degrees farenheit")
    
    #determines if -v used and provides program version information
    if args.ver:
        print("temp converter version 0.2")
        exit()

if __name__ == '__main__':
    main()