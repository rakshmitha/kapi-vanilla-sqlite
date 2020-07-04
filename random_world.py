#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    https://stackoverflow.com/questions/21014618/python-randomly-generated-ip-address-as-string
'''
import random
# import socket
# import struct
# import random
from faker import Faker  

def get_random_score(min = 0, max = 100):

    return random.randint(min, max)
    
def get_random_ip():

    faker = Faker()  
    ip_addr = faker.ipv4()  

    return ip_addr



def start():
    
    print(get_random_score(60, 100))

if __name__ == '__main__':
    start()        