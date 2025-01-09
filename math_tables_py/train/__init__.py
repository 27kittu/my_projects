#!/usr/bin/env python

from .logic import Tables, form_json, ret_json

def main(): # main function in __init__ bc, it can be imported in and out of this package
    k = Tables(16)
    print(k.start_line)
    l = 0
    while l< 30:
        k.call()
        l+=1
    k.check_correct(k.record)
    #print(k.record)
    #form_json(k.record)
    #ret_json() 


__all__=[]
