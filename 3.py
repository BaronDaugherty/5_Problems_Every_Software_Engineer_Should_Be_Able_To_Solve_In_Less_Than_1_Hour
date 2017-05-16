#Write a function that computes the list of the first 100 Fibonacci numbers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

def fib_list(a,b,c):
    #list consisting of the seeded values
    l = [a,b]

    #append the sum of two values until the supplied count
    for i in range(0, c-2):
        l.append(l[i]+l[i+1])

    #print the list items
    for i in l:
        print(i)

fib_list(0,1,100)
