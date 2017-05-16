#Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.

#this is gonna get stupid
import random
random.seed()

#lists of numbers and operators
n = ['1','','2','','3','','4','','5','','6','','7','','8','','9']
o = ['+','-','']
#lists of seen permutations and solutions
seen = [''.join(n)]
hunnid = []

#8 slots and 3 operators... 3**8 = 6561 possible permutations
while len(seen) < 6561:
    c = 1
    #pick random operator (or blank) for each open slot
    while c < len(n):
        n[c] = o[random.randrange(3)]
        c+=2
    #create the string
    st = ''.join(n)
    #add the permutation if never seen, eval it, and add any found solution
    if st not in seen:
        seen.append(st)
        su = eval(st)
        if su == 100:
            hunnid.append(st)

#print the solutions out (11 total)
print(str(len(hunnid)) + " answers found: ")
for ex in hunnid:
    print(ex + " = 100")

#This is so disgustingly abusive. I love it.
