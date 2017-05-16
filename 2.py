#Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].

def comb(a, b):
    #same algorithm for both cases...
    #elements of the shorter list get inserted into the longer at odd intervals
    #(every-other)
    if len(a) >= len(b):
        for i in range(0, len(b)):
            a.insert(i+(i+1), b[i])
        return a
    else:
        for i in range(0, len(a)):
            b.insert(i+(i+1), a[i])
        return b

l1 = [1,2,3]
l2 = ['a','b','c']

print(comb(l1, l2))
