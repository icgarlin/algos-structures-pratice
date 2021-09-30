#!/usr/bin/python2.7



def merge_sort(array): 
    arr_help = [] * len(array)
    merge_sort_helper(array, arr_help, 0, len(array)-1)

def merge_sort_helper(array, helper, start, end):
    if len(array) > 1:
        mid = len(array) / 2
        merge_sort(array, helper, start, mid)
        merge_sort(array, helper, mid+1, end) 
        merge(array, helper, start, mid, end)


def merge(array, helper, start, mid, end):
    for i in range(start, end+1): 
        helper[i] = array[i]

    helperLeft = start 
    helperRight = mid + 1
    helperCurrent = start 
    while helperLeft <= mid and helperRight <= high: 
        if helper[helperLeft] <= helper[helperRight]: 
            array[helperCurrent] = helper[helperLeft]
            helperLeft = helperLeft + 1
        else if helper[helperLeft] >= helper[helperRight]: 
            array[helperCurrent] = helper[helperRight]
            helperRight = helperRight + 1 
        
        helperCurrent = helperCurrent + 1 
