#!/usr/bin/env python3

def create_dictionary(keys, values):
    return dict(zip(keys, values))  # Convert two lists into a dictionary

def shared_values(dict1, dict2):
    return set(dict1.values()) & set(dict2.values())  # Find common values

if __name__ == '__main__':
    list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
    list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']
    
    dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
    dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
    
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    print('Shared Values:', shared_values(dict_york, dict_newnham))
