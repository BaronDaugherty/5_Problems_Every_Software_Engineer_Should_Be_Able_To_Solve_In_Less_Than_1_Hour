#Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

def main():
    #create a list of integers and pass it off
    nums = [int(i) for i in input("Enter some numbers: ").split(' ')]
    print(for_func(nums))
    print(while_func(nums))
    print(rec_func(nums))

def for_func(n):
    #total
    t = 0
    #add each element to the total and return
    for i in n:
        t+=i
    return t

def while_func(n):
    #total, counter
    t = 0
    c = 0
    #add int at index to total and increment counter, return when out of elements
    while c < len(n):
        t+=n[c]
        c+=1
    return t

def rec_func(n):
    #return the singular element
    if len(n) == 1:
        return n[0]
    else:
        #element 0 + (pass an ever shorter list down the line)
        return n[0] + rec_func(n[1:])

main()
