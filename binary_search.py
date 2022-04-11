
import random

import time

from numpy import sort
def linear_search(lis, target):
    for i in range(len(lis)):
        if target == lis[i]:
            return i
        else:
            continue
    return -1

def binary_search(lis, target):
    print(lis)
    lb =0
    ub = len(lis)-1
    while lb <=ub:
        mid = (lb+ub)//2
        if lis[mid] == target:
            return mid
        elif lis[mid]< target:
            lb = mid+1
        elif lis[mid]> target:
            ub = mid -1
    return -1

def binary_search_rec(lis, target, low=None,high = None):
    if low == None:
        low = 0
    if high == None:
        high = len(lis)-1
    if low>high:
        return -1

    midpoint = (low+high)//2
    if lis[midpoint] == target:
        return midpoint
    elif lis[midpoint] < target:
        return binary_search_rec(lis,target, midpoint+1, high)
    else:
        return binary_search_rec(lis,target, low, midpoint-1)

if __name__ == '__main__':
    list_1 = [1,3,5,7,9,11]
    target = 7
    print(linear_search(list_1,target))
    print(binary_search(list_1,target))
    print(binary_search_rec(list_1,target))

    sorted_list = set()
    length = 10000
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length,3*length))
    sorted_list= sorted(list(sorted_list))

    # start =time.time()
    # for targ in sorted_list:
    #     linear_search(sorted_list,targ)
    # end = time.time()
    # print("The time for linear search is:",(end-start)/length,"seconds")
    start1 =time.time()
    for targ in sorted_list:
        binary_search(sorted_list,targ)
    end1 = time.time()
    print("The time for binary search is:",(end1-start1)/length,"seconds")
    start2 =time.time()
    for targ in sorted_list:
        binary_search_rec(sorted_list,targ)
    end2 = time.time()
    print("The time for recursive binary search is:",(end2-start2)/length,"seconds")
