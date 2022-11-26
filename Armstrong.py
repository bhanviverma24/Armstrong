# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:29:47 2022

@author: Dell
"""

n=int(input())
def armst(n):
    r=0
    count=0
    x,y=n,n
    while x!=0:
        count=count+1
        x=x//10
    while y!=0:
        t=y%10
        r=r+t**count
        y=y//10
    if n==r:
        return "no. is armstrong"
    else:
        return "not armstrong"
armst(n)    
        
        