"""Programming assignment #1 

In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.

To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers. You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627

[TIP: before submitting, first test the correctness of your program on some small test cases of your own devising. Then post your best test cases to the discussion forums to help your fellow students!]

[Food for thought: the number of digits in each input number is a power of 2. Does this make your life easier? Does it depend on which algorithm you're implementing?]

The numeric answer should be typed in the space below. So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks.

"""


def ks_mult(x,y):
    """ FIRST ATTEMPT FAILED
    x = str(x) #convert to strings so length can be taken
    y = str(y) #same as above
    n = len(x)
    m = len(y)

    if n > m: #if x has more digits than y, pad y with zeros to the left
        dn = n - m #difference in number of digits. How many zeros to pad with
        y = '0'*dn + y
    elif m > n: #if y has more digits than x, pad x with zeros to the left
        dn = m - n
        x = '0'*dn + x

    #new lengths
    n = len(x) 
    m = len(y)
    
    #split x and y in halves (left and right halves)
    a = x[: n//2]
    b = x[n//2 :]
    c = y[: m//2]
    d = y[m//2 :]

    if (len(x) == 1 or len(y) == 1): #base case
        return int(x) * int(y)
    
    ac = ks_mult(a,c)
    bd = ks_mult(b,d)
    ad_bc = ks_mult(a+b, c+d) - int(ac) - int(bd)
    
    return int(10**2 * int(ac) + 10 * ad_bc + int(bd))
    """

    n = max(len(str(x)), len(str(y))) #find which str of ints is longer
    m = n//2 #find halfway point and floor round it

    if x < 10 or y < 10: #this is the base case, when the original numbers cant be divided by 10
        return x*y
    else: #it may not be necessary to split the program into if/else but it helps to develop visual symmetry of the base vs recursive code blocks
        

    
print(ks_mult(7583, 22903))


