#Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.

#this feels like cheating, but eh. I'll make up for it in challenge 5
from itertools import permutations

#list of integers, list for permutations
nums = (input("Enter numbers: ").split(' '))
perms = []

#add all possible permutations
for i in permutations(nums):
    perms.append(''.join(i))

#lay the cards down... smallest for bonus
print("Smallest: " + sorted(perms)[0])
print("Largest: " + sorted(perms, reverse=True)[0])
