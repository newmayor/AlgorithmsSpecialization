""" 
Programming Assignment 2
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the i^{th}ith row of the file indicates the i^{th}ith entry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading. 

"""

filepath = input("Enter path of the file of array to be read: ")
with open(filepath, "r") as abc:
    data = abc.readlines()

print(len(data))
print(type(data[3]))

def invCount(data_input):
    n = len(data_input)
    m = n // 2
    
    lefthalf = data_input[:m]
    righthalf = data_input[m:]
    
    a = invCount(lefthalf)
    b = invCount(righthalf)

    print("lefthalf size: " + str(len(lefthalf)))
    print("righthalf size: " + str(len(righthalf)))


invCount(data)