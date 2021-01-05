import math
import os
import random
import re
import sys
import statistics 


def activityNotifications(expenditure, d):
    freq = {}
    notification=0
    def find(idx):
        total_count = 0
        for i in range(201): 
            if i in freq:
                total_count = total_count + freq[i]
            if total_count >= idx:
                return i
    for i in range(len(expenditure)-1):
        if expenditure[i] in freq:
            freq[expenditure[i]]+=1
        else:
            freq[expenditure[i]]=1

        if i>=d-1:
            if d%2 ==0:
                median = (find(d//2)+find(d//2+1))/2
            else:
                median = find(d/2)

            if expenditure[i+1]>= (median*2) :
                notification +=1
                print("notification: ",notification)
            #remove the previous element from dictionary
            freq[expenditure[i-d+1]]-=1

    return notification

expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5
print(activityNotifications(expenditure, d))
