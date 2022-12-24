# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 18:12:26 2022

@author: DEEKSHA
"""

store={0:'TOI',1:'Hindu',2:'ET',3:'BM',4:'HT'}
nums=[26,20.5,34,10.5,18]
n=int(input())
def check_sum(nums, n):   
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] < n:
                a=[]
                a.append(i)
                a.append(j)
                b=[]
                for i in store:
                    if i in a:
                        b.append(store[i])
                if(len(b)==1):
                    continue
                print(b)
                a=[]
    return False

check_sum(nums,n)