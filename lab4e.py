#!/usr/bin/env python3

def is_digits(sobj):
    return sobj.isdigit()  # Check if all characters are digits

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
