#!/usr/bin/env python3

## define fibonacci sequence:
## -- Is there a formula for Fibonacci sequence?
## Answer: 
## --  In the Fibonacci sequence of numbers, each number in the 
## -- sequence is the sum of the two numbers before it, with 0 and 1 as
## -- the first two numbers.

def print_fibonacci(length):
    nums = [0,1]
    if length == 0:
        print([])
        return

    if length == 1:
        print([nums[0]])
        return

    nums = [0,1]
    f0 = nums[0]
    f1 = nums[1]
    f_new = f0 + f1 

    while len(nums) < length:
        f_new = nums[-1] + nums[-2]
        nums.append(f_new)

    print(nums)
